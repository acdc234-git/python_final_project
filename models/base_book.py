class Book:
    def __init__(self, title, author, isbn, is_borrowed = False): # is_borrowed false = 대여 가능, true = 대여 불가
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = is_borrowed
        

    def detail(self):
        return f"책 제목: {self.__title}, 저자: {self.__author}, ISBN: {self.__isbn}, "

    def get_title(self):
        return self.__title

    def get_isbn(self):
        return self.__isbn

    def get_author(self):
        return self.__author

    def get_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        if self.__is_borrowed:
            return False
        else:
            self.__is_borrowed = True

            return True
        
    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        else:
            return False