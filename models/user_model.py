from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"
    
    user_id=Column(Integer, primary_key=True, index=True)
    username=Column(String, nullable=False)
    first_name=Column(String, nullable=False)
    last_name=Column(String, nullable=False)
    password=Column(String, nullable=False)
    phone_no=Column(Integer, nullable=True)
    
    