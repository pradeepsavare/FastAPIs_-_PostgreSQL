from pydantic import BaseModel
from typing import List

class BookSchema(BaseModel):
    title: str

class AuthorCreate(BaseModel):
    name: str
    books: List[BookSchema]
