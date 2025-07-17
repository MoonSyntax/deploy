# 🦉 CodeSage – AI-Powered Pull Request Reviews for GitHub

> **CodeSage** is an intelligent GitHub App that automates code reviews using advanced AI models. It detects bugs, validates PR titles, identifies dependencies, and uncovers semantic duplication — all within the existing GitHub workflow.

---

##  Key Features

- **AI-Powered Pull Request Analysis**  
  CodeSage utilizes advanced AI models, such as Google Gemini, to automatically analyze pull request diffs, detect bugs and anti-patterns, and offer actionable suggestions for improving code quality.

- **PR Title Validation (with Notion Rules)**  
  It verifies pull request titles against dynamic, organization-defined naming rules from Notion to ensure consistency, clarity, and adherence to team standards.

- **Inline AI Suggestions**  
  The app delivers intelligent, context-aware feedback by posting inline comments directly on relevant code lines within GitHub.

- **PR Summarization**  
  CodeSage generates clear, concise summaries of code changes to help reviewers quickly understand the intent and scope of pull requests, even when large or complex.

- **Code Dependency Impact Analysis**  
  It identifies and analyzes semantic relationships between code modules to detect how proposed changes may impact other components in the system.

- **Semantic Duplicate Detection**  
  Using deep analysis, the app uncovers functionally similar code blocks across the repository, even when written differently, promoting reuse and reducing redundancy.

- **Token-Aware Diff Chunking**  
  CodeSage intelligently splits large diffs into syntax-aware segments to ensure efficient, accurate analysis without exceeding AI token limits.

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
