from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.services.book import BookService
from server.models.book import BookSchema

router = APIRouter()


@router.get("/", response_description="Gets all books")
async def get_all_books():
    books = await BookService.get_all_books()
    return {"data": books}


@router.post("/", response_description="Add a book")
async def add_book(book: BookSchema = Body(...)):
    book = jsonable_encoder(book)
    new_book = await BookService.add_book(book)
    return {"data": new_book}


@router.get("/{id}", response_description="get a book")
async def get_book_by_id(id: str):
    book = await BookService.get_by_id(id)
    return {"data": book}
