from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ---------------- CREATE COMPLAINT ----------------
class ComplaintCreate(BaseModel):
    user_id: int          # REQUIRED, logged-in user
    # name: str
    problem_type: str
    description: str
    district: str
    village: str
    door_no: str
    image_url: Optional[str] = None


# ---------------- UPDATE COMPLAINT ----------------
class ComplaintUpdate(BaseModel):
    problem_type: str
    description: str
    district: str
    village: str
    door_no: str

class ComplaintOut(BaseModel):
    id: int
    user_id: Optional[int]   # <-- allow None
    problem_type: str
    description: str
    district: str
    village: str
    door_no: str
    votes: int
    status: str
    created_at: datetime
    user_name: Optional[str] = None  # optional, default None
    phone: Optional[str] = None 
    image_url: Optional[str] = None
    email:Optional[str] = None

    model_config = {"from_attributes": True}