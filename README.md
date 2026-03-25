[日本語版はこちら](README.ja.md)

# code-reviewer-py

AI-powered Code Review Tool using Claude API

## Overview

A full-stack code review application built with Python and React.
Analyze your code from multiple perspectives using Claude AI.

## Tech Stack

**Backend**
- Python 3.14
- FastAPI
- Anthropic Claude API

**Frontend**
- React 19
- TypeScript
- Vite

## Features

- 4 review types: General / Security / Performance / Readability
- REST API with FastAPI
- Interactive UI with React

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

## Author

[HaruBoo](https://github.com/HaruBoo)
