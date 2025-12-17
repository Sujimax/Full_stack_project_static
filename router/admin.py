from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.comment_model import Comment
from models.complaint_model import Complaint
from dependancy import get_db

from schemas.status_update import StatusUpdate


admin_router=APIRouter(prefix="/admin",
                        tags=["admin"])

app = FastAPI(title="Complaint Management API")

Base.metadata.create_all(bind=engine)



@admin_router.put("/complaints/{id}")
def admin_update(id: int, data: StatusUpdate, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter_by(id=id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    
    # Update only the provided fields
    complaint.status = data.status
    db.commit()
    return {"message": "Status updated successfully"}

