from sentence_transformers import SentenceTransformer
from ..config import settings

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(settings.MODEL_NAME)
    return _model

def get_embeddings(texts):
    return get_model().encode(texts)