from fastapi import APIRouter, HTTPException
from app.schemas.book import Book

router = APIRouter()

books_db = []
book_id_counter = 1

@router.post("/")
def create_book(book: Book):
    global book_id_counter
    new_book = book.dict()
    new_book["id"] = book_id_counter
    book_id_counter += 1
    books_db.append(new_book)
    return new_book


@router.get("/")
def get_books():
    return books_db


@router.get("/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}")
def delete_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            books_db.remove(book)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
