[English](README.md)

# code-reviewer-py

> JavaのCLIツールをPython + FastAPIで再実装したAIコードレビューツール

## このプロジェクトの特徴

Java版の `code-reviewer`（CLIツール）をPythonで再実装し、FastAPIでWeb API化、さらにReactフロントエンドを追加したプロジェクト。同じコンセプトを異なる技術スタックで実装することで、言語・フレームワークへの理解を深めた。

## 機能

- 4つのレビュー観点：総合 / セキュリティ / パフォーマンス / 可読性
- CLIツール（`main.py`）— ターミナルから使用可能
- REST API（`app.py`）— FastAPIによるWebAPI
- Reactフロントエンド — ブラウザから使用可能
- モノレポ構成（backend + frontend）

## 技術スタック

**バックエンド** — Python 3.14 / FastAPI / Anthropic Claude API

**フロントエンド** — React 19 / TypeScript / Vite

## アーキテクチャ
```
CLI: python3 main.py sample.py security
         ↓
Web: ブラウザ → React → FastAPI → Claude API
```

## なぜPythonで再実装したか

Java版を作った後、AI開発の主流言語であるPythonを習得するために再実装。FastAPIのシンプルさとPythonのAIエコシステムへの親和性が選定理由。

## セットアップ

### バックエンド
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install anthropic python-dotenv fastapi uvicorn
cp .env.example .env  # ANTHROPIC_API_KEYを設定
uvicorn app:app --reload
```

### フロントエンド
```bash
cd frontend
npm install
npm run dev
```

## 関連プロジェクト

- [code-reviewer](https://github.com/HaruBoo/code-reviewer) — オリジナルのJava CLI版

## 作者

[HaruBoo](https://github.com/HaruBoo) — 東京在住、AIエンジニア志望。Claude APIを使った開発ツールを作っています。