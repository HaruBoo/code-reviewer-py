import { useState } from "react"

function App() {
  const [code, setCode] = useState("")
  const [reviewType, setReviewType] = useState("general")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)

  const handleReview = async () => {
    setLoading(true)
    setResult("")
    const res = await fetch("http://localhost:8000/review", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, review_type: reviewType }),
    })
    const data = await res.json()
    setResult(data.result)
    setLoading(false)
  }

  return (
    <div style={{ maxWidth: 800, margin: "40px auto", padding: "0 20px" }}>
      <h1>Code Reviewer</h1>

      <select
        value={reviewType}
        onChange={(e) => setReviewType(e.target.value)}
      >
        <option value="general">総合</option>
        <option value="security">セキュリティ</option>
        <option value="performance">パフォーマンス</option>
        <option value="readability">可読性</option>
      </select>

      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="レビューしたいコードを貼り付けてください"
        style={{ width: "100%", height: 200, marginTop: 16, display: "block" }}
      />

      <button onClick={handleReview} style={{ marginTop: 16 }}>
        {loading ? "レビュー中..." : "レビューする"}
      </button>

      {result && (
        <pre style={{ marginTop: 24, whiteSpace: "pre-wrap" }}>{result}</pre>
      )}
    </div>
  )
}

export default App