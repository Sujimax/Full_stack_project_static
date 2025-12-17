from pydantic import BaseModel
from typing import Optional

class ComplaintCreate(BaseModel):
    name: str
    problem_type: str
    description: str
    district: str
    village: str
    door_no: str
    image_url: Optional[str] = None


