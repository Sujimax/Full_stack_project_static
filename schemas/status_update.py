from pydantic import BaseModel
from typing import Optional

class StatusUpdate(BaseModel):
    status: str
    solved_image: Optional[str] = None
