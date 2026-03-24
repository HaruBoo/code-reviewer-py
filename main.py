import os
import sys
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# コマンドライン引数を取得
# sys.argv[0] = "main.py"（スクリプト名）
# sys.argv[1] = "sample.py"（渡したファイル名）
file_path = sys.argv[1]

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