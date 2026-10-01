# .dict() function is now renamed to .model_dump()
#
# schema_extra function within a Config class is now renamed to json_schema_extra
#
# Optional variables need a =None example: id: Optional[int] = None

from fastapi import FastAPI,Body
import uvicorn
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id : Optional[int] = None
    title :str
    author :str
    description :str
    rating : int
    published_date:int


    def __init__(self,id, title, author, description, rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str= Field(min_length=3)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=-1, lt = 6)
    published_date:int = Field(gt = 1600,lt = 2026)

    model_config = {
        "json_schema_extra": {
            "example":{
                "title":"A new Book",
                "author": "Diwas",
                "description": "A New Description of a book",
                "rating" :5,
                "published_date": 2022
            }
        }
    }

BOOKS = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien",
         description="A fantasy adventure about a hobbit's journey to reclaim treasure from a dragon.",
         rating=4, published_date=1937),

    Book(id=2, title="1984", author="George Orwell",
         description="A dystopian novel set in a totalitarian society under constant surveillance.",
         rating=4, published_date=1949),

    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee",
         description="A story about racial injustice and the loss of innocence in the American South.",
         rating=5, published_date=1960),

    Book(id=4, title="The Great Gatsby", author="F. Scott Fitzgerald",
         description="A tale of wealth, love, and the American Dream in the Jazz Age.",
         rating=3, published_date=1925),

    Book(id=5, title="Dune", author="Frank Herbert",
         description="A sci-fi epic about politics, religion, and survival on a desert planet.",
         rating=2, published_date=1965),
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/publish/")
async def get_book_by_date(published_date : int):
    books_by_dates = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_by_dates.append(book)

    return books_by_dates


@app.get("/books/{book_id}")
async def read_book(book_id :int):
    for book in BOOKS:
        if book_id == book.id:
            return book

@app.get("/books/")
async def read_book_by_rating(book_rating:int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
    if len(BOOKS) > 0 :
        book.id = BOOKS[-1].id + 1

    else:
        book.id = 1

    return book

@app.put("/books/update_book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id : int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break



if __name__ == "__main__":
    uvicorn.run(
        "books_2:app",
        host="127.0.0.1",  # Changed from 0.0.0.0 to 127.0.0.1
        port=8000,
        reload=True,

    )