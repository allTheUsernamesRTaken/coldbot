# ColdBot

## What This Is
ColdBot is a solo-use agentic AI tool that discovers small startups from
accelerator pages, scores them on approachability for cold internship outreach,
finds contacts, and drafts personalized emails. It uses a LangGraph ReAct agent
with 8 tools, RAG via pgvector, and supports both Anthropic Claude and OpenAI GPT
as the backing LLM.

## Architecture
- Frontend: React + Vite + TypeScript + Tailwind + Zustand → deployed on Vercel
- Backend: FastAPI on AWS Lambda (via Mangum) + API Gateway
- Agent: LangGraph ReAct agent with 8 tools (see backend/agent/tools/)
- Database: Supabase (Postgres + pgvector) — see database/migrations/
- Embeddings: Voyage AI (1024 dimensions) — see model strings below
- LLM: User-configurable — Anthropic Claude OR OpenAI GPT (see model strings below)

## Key Directories
- frontend/src/pages/ — main UI pages (Pipeline, Sources, Tracker, Settings)
- frontend/src/components/ — shared UI components
- backend/agent/ — LangGraph agent definition + state schema
- backend/agent/tools/ — each tool is its own file
- backend/api/ — FastAPI routes
- backend/services/ — database, embedding, LLM abstraction services
- database/migrations/ — numbered .sql files

## Conventions
- Backend: Python, type hints everywhere, async where possible
- Frontend: TypeScript strict mode, functional components only
- Agent tools: Each tool file exports a @tool-decorated async function
- Database: All timestamps are TIMESTAMPTZ. Use snake_case for columns.
- Environment variables: All secrets in .env (never committed)
  Required: SUPABASE_URL, SUPABASE_SECRET_KEY, VOYAGE_API_KEY,
  GITHUB_TOKEN. Plus one of: ANTHROPIC_API_KEY or OPENAI_API_KEY.

## LLM Abstraction
backend/services/llm.py provides get_chat_model() which returns either
ChatAnthropic or ChatOpenAI based on the LLM_PROVIDER env var.
All agent code uses this — never import ChatAnthropic directly in tools.

## Current Model Strings
These are the model strings used at the time of writing. If any fail with
a "model not found" error, check the provider's docs for current model IDs.
- Anthropic main: "claude-sonnet-4-20250514"
- Anthropic fast: "claude-haiku-4-5-20251001"
- OpenAI main: "gpt-5.4-mini"
- OpenAI fast: "gpt-5.4-nano"
- Embeddings: "voyage-4-lite" (1024 dims, Voyage AI)

## Testing
- Backend: pytest, run from backend/ directory
- Frontend: vitest
- Always test tools individually before testing the full agent flow

## Docker
- backend/Dockerfile — Lambda container image (production deployment)
- backend/Dockerfile.dev — standard Python image (local dev with hot reload)
- docker-compose.yml — local dev: runs backend on port 8000 with hot reload
- Local dev: `docker compose up` from project root
- Deploy: `./infra/deploy.ps1` builds image, pushes to ECR, updates Lambda

## Common Commands
- Frontend dev: cd frontend && npm run dev
- Backend dev: cd backend && uvicorn api.main:app --reload
- Run migrations: psql $DATABASE_URL -f database/migrations/001_init.sql
- Run agent test: cd backend && python -m pytest tests/test_agent.py -v
