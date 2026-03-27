# plain_legal — Claude Instructions

## Project overview
Legal document web app for Plateau Gardens. Users fill in a form and download a completed legal agreement as a PDF.

**Jira project:** LT (D Legal Team) — site: size-wow-education.atlassian.net
**Cloud ID:** `5d9ff9b8-e18a-4f7b-8d64-e9edf9eec2be`
**GitHub:** `git@github.com:aibistin/plain_legal.git` (SSH)

## Stack
- **Backend:** FastAPI + Jinja2 + WeasyPrint (Python 3.14, venv at `backend/.venv`)
- **Frontend:** Nuxt 3 + Vuetify 3 + MDI icons (Node 22)

## Running locally

**Backend** — must be run from inside `backend/`:
```bash
cd backend
.venv/bin/uvicorn main:app --reload
# http://localhost:8000
```

**Frontend:**
```bash
cd frontend
npm run dev
# http://localhost:3001
```

## Project structure
```
plain_legal/
├── backend/
│   ├── main.py                  # FastAPI app, CORS for localhost:3001
│   ├── requirements.txt
│   ├── models/psa.py            # Pydantic schemas (PsaKeyTerms, PsaSow, PsaFormData)
│   ├── routers/psa.py           # POST /api/psa/generate
│   ├── services/pdf.py          # Jinja2 → HTML → WeasyPrint PDF
│   └── templates/psa_cover.html # Cover page HTML template
├── frontend/
│   ├── nuxt.config.ts           # Vuetify via vite-plugin-vuetify, port 3001
│   ├── plugins/vuetify.ts       # Vuetify instance + theme
│   ├── composables/usePsa.ts    # fetch → blob → download logic
│   ├── pages/
│   │   ├── index.vue            # Landing page — template browser
│   │   └── psa/index.vue        # PSA form page (24 fields)
│   └── components/
│       ├── PsaKeyTermsForm.vue  # 17 Key Terms fields
│       └── PsaSowForm.vue       # 7 SOW fields
└── data/
    ├── templates.json           # Metadata for all 11 CommonPaper templates
    └── templates/               # Raw Markdown template files
```

## Key conventions
- Backend imports are relative to `backend/` (bare imports, not package-relative) — always run uvicorn from inside `backend/`
- Jinja2 uses `autoescape=True` — all user input is HTML-escaped in the PDF template
- PDF generation is synchronous (`def`, not `async def`) so FastAPI runs it in a thread pool
- Form child components use a local `reactive()` copy + bidirectional `watch` (upward emit + downward prop sync for reset)
- `URL.revokeObjectURL` is deferred 100ms after `anchor.click()` to avoid cancelling the download

## Available templates
11 CommonPaper templates in `data/templates/`. Only PSA is implemented; others show "Coming soon" on the landing page.

## Adding a new template
1. The template's fields are defined by `class="keyterms_link"` and `class="sow_link"` spans in the Markdown source
2. Add a Pydantic model in `backend/models/`
3. Add a Jinja2 HTML cover page in `backend/templates/`
4. Add a router in `backend/routers/` and include it in `main.py`
5. Add form components and a page in `frontend/`
6. Mark the template as `available: true` in `frontend/pages/index.vue`
