# Plain Legal

A web application for generating professional legal agreement PDFs. Users fill out a form and download a completed cover page ready to sign.

Built on open-source [CommonPaper](https://commonpaper.com) templates (CC BY 4.0).

## Features

- **Professional Services Agreement (PSA)** — fill in 24 fields across Key Terms and Statement of Work sections, download a PDF cover page
- Landing page listing all 11 CommonPaper templates (more coming)

## Stack

| Layer | Technology |
|---|---|
| Frontend | Nuxt 3, Vuetify 3, TypeScript |
| Backend | FastAPI, WeasyPrint, Jinja2 |
| Templates | CommonPaper open-source agreements |

## Getting started

### Requirements
- Python 3.11+
- Node.js 18+

### Backend

```bash
cd backend
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn main:app --reload
```

API runs at `http://localhost:8000`. Health check: `GET /health`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App runs at `http://localhost:3001`.

## Usage

1. Open `http://localhost:3001`
2. Click **Professional Services Agreement**
3. Fill in the Key Terms and Statement of Work fields
4. Click **Download PDF Cover Page**
5. Print and sign alongside the [PSA Standard Terms](https://commonpaper.com/standards/professional-services-agreement/1.0)

## Project structure

```
plain_legal/
├── backend/          # FastAPI — PDF generation API
├── frontend/         # Nuxt 3 — web interface
└── data/
    ├── templates.json          # Template metadata index
    └── templates/              # CommonPaper Markdown source files
        ├── PSA.md
        ├── Mutual-NDA.md
        ├── CSA.md
        └── ...
```

## Available templates

| Template | Status |
|---|---|
| Professional Services Agreement (PSA) | ✅ Available |
| Mutual Non-Disclosure Agreement (NDA) | Coming soon |
| Cloud Service Agreement (CSA) | Coming soon |
| Data Processing Agreement (DPA) | Coming soon |
| Service Level Agreement (SLA) | Coming soon |
| Software License Agreement | Coming soon |
| Business Associate Agreement (BAA) | Coming soon |
| AI Addendum | Coming soon |
| Pilot Agreement | Coming soon |
| Partnership Agreement | Coming soon |
| Design Partner Agreement | Coming soon |

## License

Legal templates sourced from [CommonPaper](https://github.com/CommonPaper) and used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
