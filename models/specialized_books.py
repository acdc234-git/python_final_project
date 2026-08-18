from .base_book import Book

class Paper_book(Book):
    def __init__(self, title, author, isbn, is_borrow = False):
        super().__init__(title, author, isbn)
        self.__is_borrow = False #false = 대여 가능, true = 대여 불가

    def detail(self):
        print('[일반 단행본] '+ super().detail())

    def __str__(self):
        return self.detail()

class E_book(Book):
    def __init__(self, title, author, isbn, is_borrow = False):
        super().__init__(title, author, isbn)
        self.__is_borrow = False #false = 대여 가능, true = 대여 불가

    def detail(self):
        print('[전자 도서] '+ super().detail())
        
    def __str__(self):
            return self.detail()