import os
import requests

API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def get_embeddings(texts):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": texts},
        timeout=60
    )

    response.raise_for_status()

    return response.json()