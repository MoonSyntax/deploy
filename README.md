# 🤖 CodeSage – AI-Powered Pull Request Reviews for GitHub

> **CodeSage** is an intelligent GitHub App that automates code reviews using advanced AI models. It detects bugs, validates PR titles, identifies dependencies, and uncovers semantic duplication — all within your existing GitHub workflow.

---

## 💡 Key Features

- 🔍 **AI-Powered Pull Request Analysis**  
  Uses Google Gemini and GPT-4 to review PR diffs, detect bugs, highlight anti-patterns, and recommend improvements.

- 🧠 **PR Title Validation (with Notion Rules)**  
  Automatically checks PR titles against dynamic company-specific rules stored in Notion — ensuring clarity and compliance.

- ✨ **Inline AI Suggestions**  
  Posts context-aware, line-level comments on pull requests, mimicking human-like review feedback.

- 📄 **PR Summarization**  
  Converts complex diffs into clear summaries, helping reviewers understand changes at a glance — even when token limits are exceeded.

- 🔗 **Code Dependency Impact Analysis**  
  Detects how code changes might affect other modules using Neo4j graph database for semantic relationship tracing.

- 🧬 **Semantic Duplicate Detection**  
  Powered by Graph Neural Networks and AST-based comparison — detects functionally similar code even with different structure or syntax.

- 📚 **Rule Matching with FAISS + Notion**  
  Leverages FAISS vector search and RAG to validate PR titles against evolving standards defined in Notion — even with imperfect matches.

- ⚙️ **Token-Aware Diff Chunking**  
  Efficiently handles large pull requests using Tree-sitter-based parsing and chunking to stay within LLM token limits.

---

## 📸 Screenshots

### 🔍 AI-Powered Review Summary  
![Review Summary](images/summary.png)

### 🧠 Title Rule Validation  
![Title Rule Check](images/title-check.png)

### 💬 Inline Code Feedback  
![Inline Comments](images/inline.png)

---

## ⚙️ How It Works

1. Install **CodeSage** on your GitHub organization.
2. On **pull request creation or update**:
   - Extracts PR title and code diff.
   - Validates title using rules from Notion.
   - Chunks large diffs using Tree-sitter.
   - Sends diff to Gemini/GPT for analysis.
   - Detects duplication, dependency risk, and quality issues.
   - Posts **inline comments and summary** on the PR.

---
## 🔧 Installation

👉 [**Install CodeSage from GitHub Marketplace**](https://github.com/marketplace)  
Or install directly:  
`https://github.com/apps/codesage/installations/new`

**Requirements:**
- GitHub repository access
