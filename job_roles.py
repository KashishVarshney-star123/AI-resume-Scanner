JOB_ROLES = {
    "Data Scientist": {
        "required": ["python", "machine learning", "pandas", "numpy", "scikit-learn"],
        "bonus": ["deep learning", "tensorflow", "pytorch", "sql"],
        "emoji": "🔬",
        "salary": "8-20 LPA"
    },
    "ML Engineer": {
        "required": ["python", "machine learning", "tensorflow", "pytorch"],
        "bonus": ["docker", "aws", "kubernetes", "deep learning"],
        "emoji": "🤖",
        "salary": "10-25 LPA"
    },
    "Backend Developer": {
        "required": ["python", "flask", "sql", "rest api"],
        "bonus": ["postgresql", "docker", "git", "aws"],
        "emoji": "⚙️",
        "salary": "6-18 LPA"
    },
    "Frontend Developer": {
        "required": ["react", "typescript", "javascript"],
        "bonus": ["git", "rest api", "communication"],
        "emoji": "🎨",
        "salary": "5-15 LPA"
    },
    "Full Stack Developer": {
        "required": ["python", "flask", "react", "sql"],
        "bonus": ["docker", "git", "rest api", "aws"],
        "emoji": "💻",
        "salary": "8-22 LPA"
    },
    "DevOps Engineer": {
        "required": ["docker", "kubernetes", "aws", "ci/cd"],
        "bonus": ["git", "python", "linux"],
        "emoji": "🛠️",
        "salary": "8-20 LPA"
    },
    "Data Analyst": {
        "required": ["python", "sql", "pandas", "numpy"],
        "bonus": ["matplotlib", "communication", "problem solving"],
        "emoji": "📊",
        "salary": "5-15 LPA"
    },
    "NLP Engineer": {
        "required": ["python", "nlp", "machine learning"],
        "bonus": ["deep learning", "tensorflow", "pytorch"],
        "emoji": "🗣️",
        "salary": "10-25 LPA"
    },
    "Cloud Engineer": {
        "required": ["aws", "docker", "kubernetes"],
        "bonus": ["ci/cd", "python", "git"],
        "emoji": "☁️",
        "salary": "8-20 LPA"
    },
    "Project Manager": {
        "required": ["communication", "problem solving", "agile"],
        "bonus": ["leadership", "git", "sql"],
        "emoji": "📋",
        "salary": "8-18 LPA"
    }
}

def suggest_roles(resume_skills):
    resume_lower = [s.lower() for s in resume_skills]
    suggestions = []

    for role, data in JOB_ROLES.items():
        required = data["required"]
        bonus = data["bonus"]

        # Kitni required skills match hui
        matched_required = [s for s in required if s in resume_lower]
        matched_bonus = [s for s in bonus if s in resume_lower]

        # Match percentage
        if len(required) > 0:
            match_pct = (len(matched_required) / len(required)) * 100
        else:
            match_pct = 0

        # Sirf 30%+ match wale roles dikhaao
        if match_pct >= 30:
            suggestions.append({
                "role": role,
                "emoji": data["emoji"],
                "match_pct": round(match_pct),
                "salary": data["salary"],
                "matched": matched_required + matched_bonus,
                "missing": [s for s in required if s not in resume_lower]
            })

    # Sort by match percentage
    suggestions.sort(key=lambda x: x["match_pct"], reverse=True)
    return suggestions[:5]  # Top 5 roles