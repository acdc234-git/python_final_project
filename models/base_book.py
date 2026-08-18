class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def detail(self):
        return f"책 제목: {self.__title}, 저자: {self.__author}, ISBN: {self.__isbn}, "

    def get_title(self):
        return self.__title

    def get_isbn(self):
        return self.__isbn

    def get_author(self):
        return self.__author