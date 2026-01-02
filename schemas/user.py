from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    bio: str

class UserResponse(BaseModel):
    id: int
    name: str
    bio: str

    class Config:
        from_attributes = True
