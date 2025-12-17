from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    complaint_id = Column(Integer, ForeignKey("complaints.id", ondelete="CASCADE"))
    user_id=Column(Integer, ForeignKey("users.user_id"))
    text = Column(String, nullable=False)   
    created_at = Column(DateTime, default=datetime)

    complaint = relationship("Complaint", back_populates="comments")