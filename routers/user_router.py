from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserCreate
from crud.user_crud import *
from dependencies import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create(data: UserCreate, db=Depends(get_db)):
    return create_user(db, data)

@router.get("/")
def read_all(db=Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}")
def read_one(user_id: int, db=Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user

@router.delete("/{user_id}")
def delete(user_id: int, db=Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(404, "User not found")
    return {"message": "User deleted"}

@router.put("/{user_id}")
def update(user_id: int, data: UserCreate, db=Depends(get_db)):
    user = update_user(db, user_id, data)
    if not user:
        raise HTTPException(404, "User not found")
    return user
