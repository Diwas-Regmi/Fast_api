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
async def read_all_books():
    return books

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for b in books:
        if b.get("title").lower() == book_title.lower():
            return b

@app.get("/books/")
async def read_cat(category:str):
    books_to_return = []
    for b in books:
        if b.get("category").casefold() == category.casefold():
            books_to_return.append(b)
    return books_to_return

@app.get("/books/{book_author}/")
async def book_author(book_author : str, category : str):
    books_to_return = []
    for book in books:
        if book.get("author").casefold() == book_author.casefold() and book.get("category").casefold() == category.casefold():

            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    books.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(books)):
        if books[i].get("title").casefold() == updated_book.get("title").casefold():
            books[i] = updated_book


    books.append(new_book)


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(books)):
        if books[i].get("title").casefold() == book_title.casefold():
            books.pop(i)
            break



if __name__ == "__main__":
    uvicorn.run(
        "books:app",
        host="127.0.0.1",  # Changed from 0.0.0.0 to 127.0.0.1
        port=8000,
        reload=True,

    )