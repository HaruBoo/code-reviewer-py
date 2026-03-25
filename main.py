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

# ファイル読み込み
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# レビュー観点を取得（省略可能）
review_type = sys.argv[2] if len(sys.argv) > 2 else "general"

# 観点ごとのプロンプトを定義
prompts = {
    "general":     "以下のコードを総合的にレビューしてください：\n\n",
    "security":    "以下のコードをセキュリティの観点からレビューしてください：\n\n",
    "performance": "以下のコードをパフォーマンスの観点からレビューしてください：\n\n",
    "readability": "以下のコードを可読性の観点からレビューしてください：\n\n",
}

# 無効な観点が指定された場合
if review_type not in prompts:
    print("観点は general / security / performance / readability から選んでください")
    sys.exit(1)

prompt = prompts[review_type] + code

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(message.content[0].text)