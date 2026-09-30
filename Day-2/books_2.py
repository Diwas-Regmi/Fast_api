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


    def __init__(self,id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str= Field(min_length=3)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=-1, lt = 6)

BOOKS = [
    Book(1, "The Hobbit", "J.R.R. Tolkien", "A fantasy adventure about a hobbit's journey to reclaim treasure from a dragon.", 4.8),
    Book(2, "1984", "George Orwell", "A dystopian novel set in a totalitarian society under constant surveillance.", 4.7),
    Book(3, "To Kill a Mockingbird", "Harper Lee", "A story about racial injustice and the loss of innocence in the American South.", 4.8),
    Book(4, "The Great Gatsby", "F. Scott Fitzgerald", "A tale of wealth, love, and the American Dream in the Jazz Age.", 4.4),
    Book(5, "Dune", "Frank Herbert", "A sci-fi epic about politics, religion, and survival on a desert planet.", 4.6)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
    if len(BOOKS) > 0 :
        book.id = BOOKS[-1].id +1

    else:
        book.id = 1

    return book


if __name__ == "__main__":
    uvicorn.run(
        "books_2:app",
        host="127.0.0.1",  # Changed from 0.0.0.0 to 127.0.0.1
        port=8000,
        reload=True,

    )