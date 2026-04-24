export default function ResultView({ result }) {
  return (
    <div>
      <h2>Root Causes</h2>
      <ul>
        {result.root_causes.map((c, i) => <li key={i}>{c}</li>)}
      </ul>

      <h2>Reproduction Steps</h2>
      <ul>
        {result.repro_steps.map((s, i) => <li key={i}>{s}</li>)}
      </ul>
    </div>
  );
}
