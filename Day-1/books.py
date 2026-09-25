import uvicorn
from fastapi import FastAPI

app = FastAPI(debug=True)

books =[
    {"title":"Title_1",
     "author": "Author_1",
     "category":"Science"},
    {"title":"Title_2",
     "author": "Author_2",
     "category":"history"},
    {"title":"Title_3",
     "author": "Author_3",
     "category":"fiction"},
    {"title":"Title_4",
     "author": "Author_4",
     "category":"comic"},

]

@app.get("/")
async def first_api():
    return {"message": "Hello World!"}

@app.get("/books")
async def book():
    return books

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for b in books:
        if b.get("title").lower() == book_title.lower():
            return b



if __name__ == "__main__":
    uvicorn.run(
        "books:app",
        host="127.0.0.1",  # Changed from 0.0.0.0 to 127.0.0.1
        port=8000,
        reload=True,

    )