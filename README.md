# 🦉 CodeSage – AI-Powered Pull Request Reviews for GitHub

> **CodeSage** is an intelligent GitHub App that automates code reviews using advanced AI models. It detects bugs, validates PR titles, identifies dependencies, and uncovers semantic duplication — all within the existing GitHub workflow.

---

##  Key Features

-  **AI-Powered Pull Request Analysis**  
  CodeSage leverages state-of-the-art AI models such as Google Gemini and GPT-4 to automatically analyze pull request diffs, detect potential bugs, identify anti-patterns, and provide actionable suggestions to improve code quality.

-  **PR Title Validation (with Notion Rules)**  
 It validates pull request titles against dynamic, organization-specific naming rules defined in Notion, ensuring consistency, clarity, and adherence to team conventions.

-  **Inline AI Suggestions**  
  The app provides intelligent, context-aware feedback by posting inline comments directly on the relevant lines of code, offering developers human-like guidance within the GitHub interface.
-  **PR Summarization**  
 CodeSage generates concise, readable summaries of code changes, making it easier for reviewers to grasp the overall context and purpose of a pull request — even when it spans large or complex diffs.
-  **Code Dependency Impact Analysis**  
  By tracing semantic relationships between code modules, the app assesses how a proposed change might affect other components in the system, helping teams identify hidden risks and maintain code stability.

-  **Semantic Duplicate Detection**  
  Using advanced analysis techniques, CodeSage can detect functionally similar code blocks across the repository, even when they differ in structure or syntax — enabling teams to eliminate redundancy and promote reusability.

-  **Token-Aware Diff Chunking**  
  To ensure efficient processing of large pull requests, CodeSage automatically splits diffs into manageable segments using syntax-aware parsing. This enables accurate review while staying within the token limits of AI models.

---

##  Screenshots

###  AI-Powered Review Summary  
![Review Summary](images/summary.png)

###  Title Rule Validation  
![Title Rule Check](images/title-check.png)

###  Inline Code Feedback  
![Inline Comments](images/inline.png)

---

##  How It Works

1. Install **CodeSage** on your GitHub organization.
2. On **pull request creation or update**:
   - Extracts PR title and code diff.
   - Validates title using rules from Notion.
   - Chunks large diffs using Tree-sitter.
   - Sends diff to Gemini/GPT for analysis.
   - Detects duplication, dependency risk, and quality issues.
   - Posts **inline comments and summary** on the PR.

---
##  Installation

[**Install CodeSage from GitHub Marketplace**](https://github.com/marketplace)  
Or install directly:  
`https://github.com/apps/codesage/installations/new`

**Requirements:**
- GitHub repository access

## Contact
If you encounter issues or want to contribute:

📧 Email: yourname@example.com

🌐 GitHub: github.com/yourusername/codesage
