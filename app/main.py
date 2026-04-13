from fastapi import FastAPI
from app.routes import books

app = FastAPI(title="Digital Commerce Books API")

app.include_router(books.router, prefix="/books", tags=["Books"])
