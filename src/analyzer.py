# NLP Resume analysis and parsing using SpaCy and Sentence Transformers.
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Placeholders for models
# nlp = spacy.load("en_core_web_sm")
# model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_entities(text):
    """Extract entities like Name, Email, Skills, etc. using SpaCy."""
    pass

def calculate_match_score(resume_text, job_description):
    """Calculate matching score between resume and job description using Sentence Transformers."""
    pass
