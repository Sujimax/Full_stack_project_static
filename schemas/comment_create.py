from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    complaint_id:int
    user_id:int
    text:str
    
class CommentOut(BaseModel):
    id: int
    complaint_id: int
    user_id: int
    text: str
    created_at: datetime