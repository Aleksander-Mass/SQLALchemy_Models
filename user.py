from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True) # nullable=False
    firstname = Column(String, nullable=True) # nullable=False
    lastname = Column(String, nullable=True) # nullable=False
    age = Column(Integer, nullable=True) # nullable=False
    slug = Column(String, unique=True, index=True, nullable=True) # nullable=False

    tasks = relationship('Task', back_populates='user')