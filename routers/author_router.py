from fastapi import APIRouter, Depends, HTTPException
from schemas.author import AuthorCreate
from crud.author_crud import *
from dependencies import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/")
def create(data: AuthorCreate, db=Depends(get_db)):
    return create_author(db, data)

@router.get("/")
def read_all(db=Depends(get_db)):
    return get_authors(db)

@router.get("/{author_id}")
def read_one(author_id: int, db=Depends(get_db)):
    author = get_author(db, author_id)
    if not author:
        raise HTTPException(404, "Author not found")
    return author

@router.delete("/{author_id}")
def delete(author_id: int, db=Depends(get_db)):
    if not delete_author(db, author_id):
        raise HTTPException(404, "Author not found")
    return {"message": "Author deleted"}

@router.put("/{author_id}")
def update(author_id: int, data: AuthorCreate, db=Depends(get_db)):
    author = update_author(db, author_id, data)
    if not author:
        raise HTTPException(404, "Author not found")
    return author
