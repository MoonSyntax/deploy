from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
import hmac, hashlib, os, jwt
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GITHUB_WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
GITHUB_APP_ID = os.getenv("APP_ID")
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH")

@app.post("/webhook")
async def webhook(
    request: Request,
    x_hub_signature_256: str = Header(None)
):
    body = await request.body()

    # Validate webhook secret
    if not is_valid_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Invalid signature")

    payload = await request.json()
    print("✅ Received GitHub Event:", payload.get("action", "no action"))

    return JSONResponse({"status": "Webhook received"})

def is_valid_signature(payload_body, signature_header):
    if not GITHUB_WEBHOOK_SECRET or not signature_header:
        return False
    sha_name, signature = signature_header.split('=')
    mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), msg=payload_body, digestmod=hashlib.sha256)
    return hmac.compare_digest(mac.hexdigest(), signature)

@app.get("/jwt")
def create_jwt():
    with open(PRIVATE_KEY_PATH, "r") as pem_file:
        private_key = pem_file.read()

    payload = {
        "iat": int(os.time.time()),
        "exp": int(os.time.time()) + (10 * 60),
        "iss": GITHUB_APP_ID
    }

    encoded_jwt = jwt.encode(payload, private_key, algorithm="RS256")
    return {"jwt": encoded_jwt}
