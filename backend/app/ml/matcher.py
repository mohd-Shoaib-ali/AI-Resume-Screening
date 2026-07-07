from sklearn.metrics.pairwise import cosine_similarity
from .embedding_model import get_embeddings
from .text_utils import extract_keywords

def match_resume_to_job(resume_text: str, job_text: str):
    emb = get_embeddings([resume_text, job_text])
    score = float(cosine_similarity([emb[0]], [emb[1]])[0][0]) * 100

    resume_kw = extract_keywords(resume_text)
    job_kw = extract_keywords(job_text)
    missing = sorted(list(job_kw - resume_kw))[:15]

    return round(score, 2), missing