import os
import sys
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# 引数チェック
if len(sys.argv) < 2:
    print("使い方: python3 main.py <ファイルパス>")
    sys.exit(1)

file_path = sys.argv[1]

# ファイル存在チェック
if not os.path.exists(file_path):
    print(f"エラー：{file_path} が見つかりません")
    sys.exit(1)

print(f"レビュー対象：{file_path}")

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"以下のPythonコードをレビューしてください：\n\n{code}"
        }
    ]
)

print(message.content[0].text)