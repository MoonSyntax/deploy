from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
import hmac, hashlib, os, time, jwt, httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Load environment variables
GITHUB_WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
GITHUB_APP_ID = os.getenv("APP_ID")
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH")

# Validate GitHub signature
def is_valid_signature(payload_body, signature_header):
    if not GITHUB_WEBHOOK_SECRET or not signature_header:
        return False
    try:
        sha_name, signature = signature_header.split('=')
        mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), msg=payload_body, digestmod=hashlib.sha256)
        return hmac.compare_digest(mac.hexdigest(), signature)
    except Exception:
        return False

# Generate JWT for GitHub App authentication
def generate_jwt():
    with open(PRIVATE_KEY_PATH, "r") as pem_file:
        private_key = pem_file.read()

    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + (10 * 60),
        "iss": GITHUB_APP_ID
    }

    return jwt.encode(payload, private_key, algorithm="RS256")

# Post a comment on a pull request
async def post_pr_comment(repo_full_name, pr_number, comment_body, installation_id):
    jwt_token = generate_jwt()
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json"
    }

    # Exchange JWT for installation access token
    async with httpx.AsyncClient() as client:
        token_resp = await client.post(
            f"https://api.github.com/app/installations/{installation_id}/access_tokens",
            headers=headers
        )
        token_resp.raise_for_status()
        token = token_resp.json()["token"]

        # Post the comment
        comment_url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"
        comment_headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json"
        }
        comment_resp = await client.post(
            comment_url,
            headers=comment_headers,
            json={"body": comment_body}
        )
        comment_resp.raise_for_status()

# Webhook route
@app.post("/webhook")
async def webhook(request: Request, x_hub_signature_256: str = Header(None)):
    body = await request.body()

    # Validate webhook signature
    if not is_valid_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Invalid signature")

    payload = await request.json()
    print("✅ Received GitHub Event:", payload.get("action", "no action"))

    # Handle new pull request
    if payload.get("action") == "opened" and "pull_request" in payload:
        pr = payload["pull_request"]
        repo = payload["repository"]["full_name"]
        pr_number = pr["number"]
        installation_id = payload["installation"]["id"]

        await post_pr_comment(repo, pr_number, "👋 Hello from FastAPI GitHub App!", installation_id)

    return JSONResponse({"status": "Webhook received"})

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}
