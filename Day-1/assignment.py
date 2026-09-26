import uvicorn
from fastapi import FastAPI,Body

app = FastAPI(debug=True)

books =[
    {"title":"Title_1",
     "author": "Author_2",
     "category":"Science"},
    {"title":"Title_2",
     "author": "Author_1",
     "category":"history"},
    {"title":"Title_3",
     "author": "Author_3",
     "category":"fiction"},
    {"title":"Title_4",
     "author": "Author_2",
     "category":"comic"},

]

@app.get("/")
async def first_api():
    return {"message": "Hello World!"}

@app.get("/books")
async def get_all_books():
    return books

@app.get("/books/{author}")
async def get_author(author : str):
    books_new = []
    for book in books:
        if book.get("author").casefold() == author.casefold():
            books_new.append(book)

    return books_new



if __name__ == "__main__":
    uvicorn.run(
        "assignment:app",
        host="127.0.0.1",  # Changed from 0.0.0.0 to 127.0.0.1
        port=8000,
        reload=True,

    )