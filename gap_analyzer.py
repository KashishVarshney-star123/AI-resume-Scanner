from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def find_skill_gap(resume_skills, jd_skills):
    """Analyzes the gap between resume skills and job description (JD) skills.
    
    Calculates semantic match percentage using sentence embeddings and classifies 
    skills into matched and missing lists.
    
    Args:
        resume_skills (list): List of skills extracted from the resume.
        jd_skills (list): List of skills extracted from the job description.
        
    Returns:
        dict: A dictionary containing:
            - 'matched' (list): List of JD skills present in the resume.
            - 'missing' (list): List of JD skills absent from the resume.
            - 'match_percent' (float): Cosine similarity score mapped to [0.0, 100.0].
    """
    # Normalize and filter inputs
    resume_skills_clean = [s.strip() for s in resume_skills if s.strip()]
    jd_skills_clean = [s.strip() for s in jd_skills if s.strip()]
    
    # Handle edge cases
    if not jd_skills_clean:
        return {
            "matched": [],
            "missing": [],
            "match_percent": 100.0 if resume_skills_clean else 0.0
        }
    if not resume_skills_clean:
        return {
            "matched": [],
            "missing": sorted(list(set(jd_skills_clean))),
            "match_percent": 0.0
        }
        
    # Check matches case-insensitively
    resume_lower = {s.lower() for s in resume_skills_clean}
    
    matched = []
    missing = []
    
    for skill in jd_skills_clean:
        if skill.lower() in resume_lower:
            matched.append(skill)
        else:
            missing.append(skill)
            
    # Calculate cosine similarity between skill sets
    # Convert lists to comma-separated strings to represent the skill set context
    resume_str = ", ".join(resume_skills_clean)
    jd_str = ", ".join(jd_skills_clean)
    
    # Encode and calculate similarity
    embeddings = model.encode([resume_str, jd_str])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    # Convert similarity score to a percentage scale [0.0, 100.0]
    match_percent = max(0.0, min(100.0, float(similarity) * 100.0))
    
    return {
        "matched": sorted(list(set(matched))),
        "missing": sorted(list(set(missing))),
        "match_percent": round(match_percent, 2)
    }
