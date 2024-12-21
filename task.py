from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True) # nullable=False
    content = Column(String, nullable=True) # nullable=False
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True) #nullable=False
    slug = Column(String, unique=True, index=True, nullable=True) # nullable=False

    user = relationship('User', back_populates='tasks')