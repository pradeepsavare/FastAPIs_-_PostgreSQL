from fastapi import FastAPI
from database import Base, engine
from routers import user_router, author_router, student_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Professional FastAPI PostgreSQL Project")

app.include_router(user_router.router)
app.include_router(author_router.router)
app.include_router(student_router.router)
