from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    problem_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    district = Column(String, nullable=False)
    village = Column(String, nullable=False)
    door_no = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    solved_image = Column(String, nullable=True)
    votes = Column(Integer, default=0)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    comments = relationship("Comment", back_populates="complaint", cascade="all, delete-orphan")



