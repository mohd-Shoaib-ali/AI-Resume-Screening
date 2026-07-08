from sentence_transformers import SentenceTransformer
from ..config import settings

_model = None

def get_model():
    global _model

    if _model is None:
        print("Loading AI model...")
        _model = SentenceTransformer(settings.MODEL_NAME)

    return _model


def get_embeddings(texts):
    model = get_model()
    return model.encode(texts)