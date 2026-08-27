function ResultsScreen({ results, onBack }) {
  return (
    <div className="results-screen">
      <h1>🎯 Tes métiers recommandés</h1>

      {results.map((job) => (
        <div key={job.id} className="result-row">
          <div className="result-header">
            <span>{job.name}</span>
            <span>{job.score}%</span>
          </div>
          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{ width: `${job.score}%` }}
            />
          </div>
        </div>
      ))}

      <button onClick={onBack}>← Modifier mes compétences</button>
    </div>
  );
}

export default ResultsScreen;