from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from fastapi.responses import HTMLResponse

from models import Student

app = FastAPI()   # 👈 MUST come before using @app

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("index.html", "r") as file:
        return file.read()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/predict")
def predict(math: int, english: int, db: Session = Depends(get_db)):
    total = math + english
    result = "Pass" if total >= 70 else "Fail"

    student = Student(math=math, english=english, result=result)
    db.add(student)
    db.commit()
    db.refresh(student)

    return {"id": student.id, "result": result}

@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
