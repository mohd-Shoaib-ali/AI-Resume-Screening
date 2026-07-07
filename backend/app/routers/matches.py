from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Resume, Job, MatchResult
from ..schemas import MatchRequest
from ..ml.matcher import match_resume_to_job

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.post("/")
def create_match(payload: MatchRequest, db: Session = Depends(get_db)):
    resume = db.query(Resume).filter(Resume.id == payload.resume_id).first()
    job = db.query(Job).filter(Job.id == payload.job_id).first()

    if not resume or not job:
        raise HTTPException(status_code=404, detail="resume or job not found")

    score, missing = match_resume_to_job(resume.text, job.description)

    row = MatchResult(
        resume_id=resume.id,
        job_id=job.id,
        score=score,
        missing_skills=", ".join(missing)
    )
    db.add(row)
    db.commit()
    db.refresh(row)

    return {
        "resume_id": resume.id,
        "job_id": job.id,
        "match_score": score,
        "missing_skills": missing
    }

@router.get("/")
def list_matches(db: Session = Depends(get_db)):
    rows = db.query(MatchResult).order_by(MatchResult.created_at.desc()).all()
    return [
        {
            "id": m.id,
            "resume_id": m.resume_id,
            "job_id": m.job_id,
            "score": m.score,
            "missing_skills": m.missing_skills
        }
        for m in rows
    ]