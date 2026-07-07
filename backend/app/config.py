import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")

settings = Settings()