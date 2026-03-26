[日本語版](README.ja.md)

# code-reviewer-py

> Python + FastAPI implementation of an AI code reviewer — rebuilt from a Java CLI tool

## What makes this different

This project started as a Java CLI tool (`code-reviewer`), then rebuilt in Python with FastAPI to add a web API layer and React frontend. The goal was to demonstrate the same concept across different tech stacks.

## Features

- 4 review types: General / Security / Performance / Readability
- CLI tool (`main.py`) for terminal use
- REST API (`app.py`) with FastAPI
- React frontend for browser use
- Monorepo architecture (backend + frontend)

## Tech Stack

**Backend** — Python 3.14 / FastAPI / Anthropic Claude API

**Frontend** — React 19 / TypeScript / Vite

## Architecture
```
CLI: python3 main.py sample.py security
         ↓
Web: Browser → React → FastAPI → Claude API
```

## Why rebuild in Python?

After building the Java version, Python was the natural next step for AI development. FastAPI's simplicity and Python's dominance in the AI ecosystem made it an ideal choice.

## Getting Started

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install anthropic python-dotenv fastapi uvicorn
cp .env.example .env  # Add your ANTHROPIC_API_KEY
uvicorn app:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Related

- [code-reviewer](https://github.com/HaruBoo/code-reviewer) — Original Java CLI version

## Author

[HaruBoo](https://github.com/HaruBoo) — Aspiring AI engineer based in Tokyo. Building developer tools with Claude API.