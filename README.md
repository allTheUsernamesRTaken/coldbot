# ColdBot

AI-powered cold outreach assistant.

## Structure

```
coldbot/
├── frontend/     React + Vite + TypeScript + Tailwind v4
├── backend/      Python — FastAPI + LangGraph agent, deployed via Mangum on AWS Lambda
├── database/     SQL migration files for Supabase
└── infra/        AWS deployment scripts
```

## Getting started

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
# Activate the venv
.venv/Scripts/activate        # Windows
source .venv/bin/activate     # macOS/Linux

uvicorn src.coldbot.main:app --reload
```
