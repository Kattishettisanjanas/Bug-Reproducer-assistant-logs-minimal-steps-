export async function analyzeLogs(logText) {
  const res = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ log_text: logText })
  });
  return res.json();
}
