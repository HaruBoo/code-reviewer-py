import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewRequest(BaseModel):
    code: str
    review_type: str = "general"

@app.get("/")
def root():
    return {"message": "Code Reviewer API"}

@app.post("/review")
def review(req: ReviewRequest):
    prompts = {
        "general":     "以下のコードを総合的にレビューしてください：\n\n",
        "security":    "以下のコードをセキュリティの観点からレビューしてください：\n\n",
        "performance": "以下のコードをパフォーマンスの観点からレビューしてください：\n\n",
        "readability": "以下のコードを可読性の観点からレビューしてください：\n\n",
    }
    prompt = prompts[req.review_type] + req.code
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return {"result": message.content[0].text}