import { useState } from "react";
import LogInput from "./components/LogInput";
import ResultView from "./components/ResultView";
import { analyzeLogs } from "./api";

export default function App() {
  const [result, setResult] = useState(null);

  const handleAnalyze = async (logText) => {
    const data = await analyzeLogs(logText);
    setResult(data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Bug Reproducer</h1>
      <LogInput onAnalyze={handleAnalyze} />
      {result && <ResultView result={result} />}
    </div>
  );
}
