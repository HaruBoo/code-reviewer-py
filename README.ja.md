[English](README.md)

# code-reviewer-py

Claude APIを使ったAIコードレビューツール

## 概要

PythonとReactで作ったフルスタックのコードレビューアプリ。
Claude AIを使って、複数の観点からコードを分析できます。

## 技術スタック

**バックエンド**
- Python 3.14
- FastAPI
- Anthropic Claude API

**フロントエンド**
- React 19
- TypeScript
- Vite

## 機能

- 4つのレビュー観点：総合 / セキュリティ / パフォーマンス / 可読性
- FastAPIによるREST API
- ReactによるインタラクティブなUI

## セットアップ

### バックエンド
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install anthropic python-dotenv fastapi uvicorn
cp .env.example .env  # ANTHROPIC_API_KEYを追加
uvicorn app:app --reload
```

### フロントエンド
```bash
cd frontend
npm install
npm run dev
```

## 作者

[HaruBoo](https://github.com/HaruBoo)