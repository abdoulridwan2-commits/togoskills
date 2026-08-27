export function computeScore(userSkillIds, job) {
  const totalWeight = job.requiredSkills.reduce((sum, s) => sum + s.weight, 0);
  const matchedWeight = job.requiredSkills
    .filter((s) => userSkillIds.includes(s.skillId))
    .reduce((sum, s) => sum + s.weight, 0);

  return Math.round((matchedWeight / totalWeight) * 100);
}

export function matchAllJobs(userSkillIds, jobsList) {
  return jobsList
    .map((job) => ({ ...job, score: computeScore(userSkillIds, job) }))
    .sort((a, b) => b.score - a.score);
}