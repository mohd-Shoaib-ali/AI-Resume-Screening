from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Resume
from ..utils.file_parser import extract_text_from_file, clean_text

router = APIRouter(prefix="/resumes", tags=["Resumes"])

@router.post("/upload")
async def upload_resume(
    name: str = Form(...),
    email: str = Form(""),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    raw = await file.read()
    text = clean_text(extract_text_from_file(raw, file.filename))
    if not text:
        raise HTTPException(status_code=400, detail="Could not extract text from file")

    obj = Resume(name=name, email=email, text=text)
    db.add(obj)
    db.commit()
    db.refresh(obj)

    return {"message": "resume uploaded", "resume_id": obj.id}

@router.get("/")
def list_resumes(db: Session = Depends(get_db)):
    rows = db.query(Resume).order_by(Resume.created_at.desc()).all()
    return [
        {"id": r.id, "name": r.name, "email": r.email, "created_at": str(r.created_at)}
        for r in rows
    ]