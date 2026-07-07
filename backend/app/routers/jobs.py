from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Job
from ..schemas import JobCreate

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/")
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    obj = Job(title=payload.title, description=payload.description)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return {"message": "job created", "job_id": obj.id}

@router.get("/")
def list_jobs(db: Session = Depends(get_db)):
    rows = db.query(Job).order_by(Job.created_at.desc()).all()
    return [
        {"id": j.id, "title": j.title, "created_at": str(j.created_at)}
        for j in rows
    ]