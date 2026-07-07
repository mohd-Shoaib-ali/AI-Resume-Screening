import re

def extract_keywords(text: str):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9+.#-]+", text.lower())
    stop = {
        "the", "and", "for", "with", "from", "that", "this", "using",
        "into", "are", "was", "you", "your", "job", "resume", "role"
    }
    return set(w for w in words if w not in stop and len(w) > 2)