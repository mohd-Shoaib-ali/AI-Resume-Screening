from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import resumes, jobs, matches

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Screening Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resumes.router)
app.include_router(jobs.router)
app.include_router(matches.router)

@app.get("/")
def root():
    return {"message": "AI Resume Screening Platform is running"}

@app.get("/health")
def health():
    return {"status": "ok"}