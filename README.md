Here's the updated version of your `README.md` with a thank you note included:

---

```markdown
# 🚀 AI-Powered Job Application Assistant

An end-to-end AI-driven workflow that automates the job application process—from sourcing job listings to sending personalized outreach emails. Built with [CrewAI](https://docs.crewai.com/) and powered by **Gemini** and **Groq**, this assistant streamlines your job search with precision and personalization.

---

## 🔧 Features

- **Automated Job Sourcing** – Finds job postings based on your preferences  
- **Company Research** – Enriches job data with company and HR info  
- **Resume Tailoring** – Customizes your resume for better ATS compatibility  
- **Email Drafting** – Generates personalized outreach emails and compiles them into Excel

---

## 🔄 Workflow Overview

```text
User Input
   ↓
[1] Job Sourcing Agent
   → Jobs List
   ↓
[2] Company Research Agent
   → Company Info + HR Emails
   ↓
[3] Resume Tailoring Agent
   → Tailored Resume Stored
   ↓
[4] Email Drafting Agent
   → Excel with all details (with Resume Attached)
```

---

## 🛠 Installation & Setup

### Requirements

- Python >= 3.10 and < 3.13  
- `uv` for dependency and tool management

### Install Dependencies

```bash
pip install "crewai[tools]>=0.114.0,<1.0.0"
pip install google-generativeai>=0.8.5
pip install groq>=0.22.0
pip install linkup-sdk>=0.2.4
```

### Install `uv` (if needed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Or for Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 🚀 Getting Started

### Create Your Project

```bash
uv tool install crewai
crewai create crew <your_project_name>
```

### Project Structure

```
my_project/
├── .env
├── src/
│   └── my_project/
│       ├── main.py
│       ├── crew.py
│       └── config/
│           ├── agents.yaml
│           └── tasks.yaml
```

### Run Your Crew

```bash
crewai install
crewai run
```

---

## 📄 License

MIT License

---

## 🙏 Acknowledgments

A special thanks to **Vickybytes** for the **AI Agents Unleashed: Hiring Challenge** + Prizes + Payouts, and the opportunity to participate in this amazing contest. Win 30K!

---
```

Let me know if you need any further adjustments!
