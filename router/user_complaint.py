from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependancy import get_db
from models.complaint_model import Complaint
from models.comment_model import Comment
from schemas.complaint_create import ComplaintCreate
from schemas.complaint_update import ComplaintUpdate
from schemas.comment_create import CommentCreate

user_complaint = APIRouter(
    prefix="/complaints",
    tags=["complaints"]
)

@user_complaint.post("/")
def create_complaint(new: ComplaintCreate, db: Session = Depends(get_db)):
    complaint = Complaint(**new.model_dump()) 
    db.add(complaint)
    db.commit()
    db.refresh(complaint)
    return complaint

@user_complaint.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Complaint).all()


@user_complaint.get("/comments")
def get_comment(db: Session = Depends(get_db)):
    return db.query(Comment).all()


@user_complaint.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter_by(id=id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return complaint


@user_complaint.put("/{id}")
def update_complaint(id: int, updated: ComplaintUpdate, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter_by(id=id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    complaint.problem_type=updated.problem_type
    complaint.description=updated.description
    complaint.district=updated.district
    complaint.village=updated.village
    complaint.door_no=updated.door_no   
    db.commit()
    db.refresh(complaint)
    return {"message": "Updated successfully"}


@user_complaint.delete("/{id}")
def delete_complaint(id: int, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter_by(id=id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    db.delete(complaint)
    db.commit()
    return {"message": "Complaint deleted successfully"}


@user_complaint.post("/{id}/vote")
def vote(id: int, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter_by(id=id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    complaint.votes += 1
    db.commit()
    db.refresh(complaint)
    return {"message": "Vote added"}


@user_complaint.post("/comment")
def add_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    new_comment = Comment(**comment.model_dump())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message": "Comment added"}


@user_complaint.delete("/{id}")
def delete_comment(id:int, db:Session = Depends(get_db)):
    comment = db.query(Comment).filter_by(id=id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="comment not found")
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}


