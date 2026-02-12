from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    math = Column(Integer)
    english = Column(Integer)
    result = Column(String)
