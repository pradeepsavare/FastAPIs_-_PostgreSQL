from fastapi import APIRouter, Depends, HTTPException
from schemas.student import StudentCreate
from crud.student_crud import *
from dependencies import get_db

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def create(data: StudentCreate, db=Depends(get_db)):
    return create_student(db, data)

@router.get("/")
def read_all(db=Depends(get_db)):
    return get_students(db)

@router.get("/{student_id}")
def read_one(student_id: int, db=Depends(get_db)):
    student = get_student(db, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    return student

@router.delete("/{student_id}")
def delete(student_id: int, db=Depends(get_db)):
    if not delete_student(db, student_id):
        raise HTTPException(404, "Student not found")
    return {"message": "Student deleted"}

@router.put("/{student_id}")
def update(student_id: int, data: StudentCreate, db=Depends(get_db)):
    student = update_student(db, student_id, data)
    if not student:
        raise HTTPException(404, "Student not found")
    return student
