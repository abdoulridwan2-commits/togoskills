import { useState } from "react";
import skillsData from "../data/skills.json";

function SkillSelector({ onAnalyze }) {
  const [selectedSkillIds, setSelectedSkillIds] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  const filteredSkills = skillsData.filter((skill) =>
    skill.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  function toggleSkill(skillId) {
    setSelectedSkillIds((prev) =>
      prev.includes(skillId)
        ? prev.filter((id) => id !== skillId)
        : [...prev, skillId]
    );
  }

  function handleAnalyze() {
    onAnalyze(selectedSkillIds);
  }

  return (
    <div className="skill-selector">
      <h1>TogoSkills</h1>
      <p>Trouve les métiers qui correspondent à ton profil</p>

      <input
        type="text"
        placeholder="🔍 Rechercher une compétence..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <div className="skill-grid">
        {filteredSkills.map((skill) => (
          <label key={skill.id} className="skill-checkbox">
            <input
              type="checkbox"
              checked={selectedSkillIds.includes(skill.id)}
              onChange={() => toggleSkill(skill.id)}
            />
            {skill.name}
          </label>
        ))}
      </div>

      <button
        onClick={handleAnalyze}
        disabled={selectedSkillIds.length === 0}
      >
        Analyser mon profil ({selectedSkillIds.length} sélectionnée{selectedSkillIds.length > 1 ? "s" : ""})
      </button>
    </div>
  );
}

export default SkillSelector;