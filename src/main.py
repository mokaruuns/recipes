from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


@app.get('/')
def home():
    return {"key": "value"}


@app.get('/{pk}')
def get_item(pk: int):
    return {"key": pk}


@app.post('/book')
def create_book(item: Book):
    return item


@app.get("/book")
def get_book(q: str = Query(None)):
    return q
