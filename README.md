#  InternMatch — Smart Internship Portal with Skill Matching

> *Bridging the gap between student potential and industry opportunity through AI-powered skill matching.*

---

## Problem Statement

Students and fresh graduates struggle to find internships that align with their actual skills, while companies receive hundreds of irrelevant applications. Traditional portals rely on manual searching with no intelligent filtering — resulting in mismatches, wasted time, and missed opportunities on both sides.

**InternMatch** solves this by automatically analyzing a student's resume, extracting their skills, and matching them to internships based on real job requirements — not just keywords.

---

## What It Does

A full-stack web platform that intelligently connects students to internships through:

| Module | Description |
|--------|-------------|
| **Resume Analyzer** | Parses PDF/DOCX resumes, extracts 100+ skills automatically |
| **Smart Skill Matcher** | Matches extracted skills against live internship requirements |
| **Match Score Engine** | Ranks internships by compatibility percentage per student |
| **AI Roadmap Generator** | Suggests what skills to learn to qualify for top internships |
| **Student Dashboard** | Personalized feed of matched internships with gap analysis |
| **Auth System** | JWT-based login — each student's data stays private |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI (Python 3.11+) |
| **Frontend** | Vanilla HTML/CSS/JS + Tailwind CSS |
| **AI / LLM** | Groq `llama-3.3-70b-versatile` (free tier) |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Auth** | JWT + bcrypt |
| **Resume Parsing** | pdfplumber, python-docx |
| **Skill Extraction** | Custom NLP dictionary (100+ skills) |
| **Async HTTP** | httpx |

---

## How the Matching Works

```
Student uploads resume
        ↓
Resume Parser extracts raw text (PDF/DOCX/TXT)
        ↓
Skill Extractor detects skills from 100+ skill dictionary
        ↓
Matching Algorithm compares student skills vs job requirements
        ↓
Match Score = (matched skills / required skills) × 100%
        ↓
Internships ranked by score → displayed on dashboard
        ↓
AI Roadmap fills the skill gaps for unqualified listings
```

---

## 📁 Project Structure

```
intern-match/
├── backend/
│   ├── main.py                   # FastAPI entry point
│   ├── database.py               # SQLAlchemy engine
│   ├── models.py                 # ORM models
│   ├── auth/
│   │   ├── router.py             # /auth endpoints
│   │   └── utils.py              # JWT + bcrypt
│   ├── api/
│   │   ├── resume.py             # Resume upload & analysis
│   │   ├── internships.py        # Internship listing & matching
│   │   └── roadmap.py            # AI roadmap + chatbot
│   └── services/
│       ├── resume_parser.py      # PDF/DOCX text extraction
│       ├── skill_extractor.py    # Skill detection engine
│       ├── internship_matcher.py # Core matching algorithm
│       └── groq_service.py       # LLM integration
└── frontend/
    ├── index.html                # Landing page
    ├── login.html / register.html
    ├── dashboard.html            # Matched internships feed
    ├── resume.html               # Upload & analyze resume
    └── roadmap.html              # AI skill roadmap
```

---

##  Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Shreyashio/Something_Hackathonix-2.0
cd career-platform/backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Groq API key (free at console.groq.com)
echo "GROQ_API_KEY=your_key_here" > .env

# 4. Start the server
uvicorn main:app --reload

# 5. Open the frontend
open ../frontend/index.html
```
---

##  Key Highlights

-  **100% Free to run** — No paid APIs, Groq free tier (50 req/min)
-  **No build step** — Pure HTML/JS frontend, open directly in browser
-  **Mobile responsive** — Works on any device
-  **Private by design** — JWT auth, user data isolated
-  **Actionable output** — Match scores + skill gap roadmap, not generic advice

---

##  Hackathon PS Alignment

| PS Requirement | Implementation |
|----------------|----------------|
| Match students with internships | Skill-based matching algorithm with % score |
| Based on skills |  Auto-extracted from resume using NLP |
| Resume keywords |  PDF/DOCX parser + 100+ skill dictionary |
| Job requirements |  Matched against structured internship listings |
| Web platform |  Full-stack FastAPI + HTML/JS |

---

