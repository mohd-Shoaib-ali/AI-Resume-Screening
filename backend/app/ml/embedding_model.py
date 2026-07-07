from sentence_transformers import SentenceTransformer
from ..config import settings

model = SentenceTransformer(settings.MODEL_NAME)

def get_embeddings(texts):
    return model.encode(texts)