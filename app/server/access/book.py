from fastapi import Request
from server.access import book_collection
from bson.objectid import ObjectId


class BookAccess:
    """
    A class to handle all database-related operations for books
    """

    @staticmethod
    async def get_all_books():
        '''Get all the books from the database'''
        books = []
        async for book in book_collection.find():
            books.append({"title": book["title"], "author": book["author"]})
        return books

    @staticmethod
    async def add_book(book_data: dict) -> dict:
        """Add a new book into to the database"""
        book = await book_collection.insert_one(book_data)
        new_book = await book_collection.find_one({"_id": book.inserted_id})
        return {"title": new_book["title"], "author": new_book["author"]}

    @staticmethod
    async def get_book_by_id(id: str):
        '''Get a book by its id'''
        book = await book_collection.find_one({"_id": ObjectId(id)})
        if book:
            return {"title": book["title"], "author": book["author"]}
  
