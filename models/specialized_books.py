from .base_book import Book

class Paper_book(Book):
    def __init__(self, title, author, isbn, is_borrow = False):
        super().__init__(title, author, isbn)
        self.__is_borrow = False #false = 대여 가능, true = 대여 불가

    def detail(self):
        return '[일반 단행본] '+ super().detail() + '대여 여부: ' + ('대여 중' if self.__is_borrow else '대여 가능')

    def __str__(self):
        return self.detail()

class E_book(Book):
    def __init__(self, title, author, isbn, is_borrow = False):
        super().__init__(title, author, isbn)
        self.__is_borrow = False #false = 대여 가능, true = 대여 불가

    def detail(self):
        return '[전자 도서] '+ super().detail() + '대여 여부: ' + ('대여 중' if self.__is_borrow else '대여 가능')
        
    def __str__(self):
            return self.detail()