from sentence_transformers import SentenceTransformer
from ..config import settings

model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return model
def get_embeddings(texts):
    return model.encode(texts)