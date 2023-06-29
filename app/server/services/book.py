from server.access.book import BookAccess

class BookService:
    '''
    A service class for handling book operations.
    '''

    @staticmethod
    async def get_all_books():
        books = await BookAccess.get_all_books()
        return books
    
    @staticmethod
    async def add_book(book_data: dict):
        new_book = await BookAccess.add_book(book_data)
        return new_book
    

    @staticmethod
    async def get_by_id(id: str):
        book = await BookAccess.get_book_by_id(id)
        return book