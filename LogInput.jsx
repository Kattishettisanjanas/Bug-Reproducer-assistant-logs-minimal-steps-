import { useState } from "react";

export default function LogInput({ onAnalyze }) {
  const [text, setText] = useState("");

  return (
    <div>
      <textarea
        rows={10}
        cols={80}
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={() => onAnalyze(text)}>Analyze</button>
    </div>
  );
}
