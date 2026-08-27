import { useState } from "react";
import SkillSelector from "./components/SkillSelector";
import ResultsScreen from "./components/ResultsScreen";
import jobsData from "./data/jobs.json";
import { matchAllJobs } from "./utils/matching";
import "./App.css";

function App() {
  const [results, setResults] = useState(null);

  function handleAnalyze(selectedSkillIds) {
    const matched = matchAllJobs(selectedSkillIds, jobsData);
    setResults(matched);
  }

  function handleBack() {
    setResults(null);
  }

  return (
    <div className="app">
      {results === null ? (
        <SkillSelector onAnalyze={handleAnalyze} />
      ) : (
        <ResultsScreen results={results} onBack={handleBack} />
      )}
    </div>
  );
}

export default App;