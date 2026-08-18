class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def detail(self):
        print(f"책 제목: {self.__title}, 저자: {self.author}, ISBN: {self.__isbn}")