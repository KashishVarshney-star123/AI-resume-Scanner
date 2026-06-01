import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy NLP model, download if it is missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    import sys
    print("Downloading spaCy models...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Define skills categorized across 6 areas
SKILLS_DB = [
    # Programming
    "Python", "Java", "C++", "C#", "JavaScript", "TypeScript", "Ruby", "Go", "Rust", "Swift", "Kotlin", "PHP", "R", "Scala",
    
    # Web
    "HTML", "CSS", "React", "Angular", "Vue", "Node.js", "Express", "Flask", "Django", "FastAPI", "ASP.NET", "Bootstrap", "Tailwind", "GraphQL", "REST API",
    
    # Database
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "SQLite", "Oracle", "Cassandra", "DynamoDB", "MariaDB", "Firebase", "Neo4j",
    
    # ML/AI
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "TensorFlow", "PyTorch", "Keras", "Scikit-Learn", "Pandas", "NumPy", "SciPy", "Hugging Face", "LLMs", "Generative AI",
    
    # Cloud / DevOps
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Terraform", "CI/CD", "Git", "Jenkins", "Ansible", "Serverless",
    
    # Soft Skills
    "Leadership", "Communication", "Teamwork", "Problem Solving", "Time Management", "Critical Thinking", "Adaptability", "Collaboration", "Project Management"
]

# Configure PhraseMatcher for case-insensitive matching
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILLS_DB]
matcher.add("SkillsMatcher", patterns)

def extract_skills(text):
    """Extracts unique skills matching the SKILLS_DB from input text.
    
    Args:
        text (str): Resume or description text to scan.
        
    Returns:
        list: Sorted list of canonical skill names found in the text.
    """
    if not text:
        return []
        
    doc = nlp(text)
    matches = matcher(doc)
    
    found_skills = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        matched_text = span.text.lower()
        
        # Map the matched text back to its exact case-sensitive entry in SKILLS_DB
        for skill in SKILLS_DB:
            if skill.lower() == matched_text:
                found_skills.add(skill)
                break
                
    return sorted(list(found_skills))
