from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str

class MatchRequest(BaseModel):
    resume_id: int
    job_id: int