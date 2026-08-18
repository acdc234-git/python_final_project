from models.specialized_books import Paper_book, E_book

def register_book(books,isbns):
    print('신규 도서 등록 메뉴 입니다. 각 항목을 입력해주세요')
    print('책 이름: ')
    title = str(input())
    print('저자: ')
    author = str(input())
    print('ISBN: ')
    while True:
        isbn = str(input())
        if isbn in books:
            print('중복된 ISBN 입니다.')
        else:
            break
    print('책 타입 (일반 or 전자도서):')
    while True:
        type = str(input())
        if type in ['일반','전자도서']:
            if type == '일반':
                ebook = False
            else:
                ebook = True
            break
        else:
            print('일반 혹은 전자도서로 입력해주세요')
    if ebook:
        new_book = E_book(title,author,isbn)
    else:
        new_book = Paper_book(title,author,isbn)
    books[isbn] = new_book
    isbns.add(isbn)

def show_book(books):
    for book in books.values():
        print(book)

def search_book(books):
    found = False
    while True:
        hello('책의 검색 방법을 입력해주세요.')
        print('1. 책 제목')
        print('2. ISBN')
        print('3. 저자')
        print('4. 메인으로')
        search = str(input())

        if search == '1':
            print('찾는 책의 제목을 입력해주세요.')
            search = str(input())
            for book in books.values():
                if book.get_title() == search:
                    print(book)                     # book 객체기 때문에 __str__ 이 작동
                    found = True
            if not found:    
                print('일치하는 책이 없습니다\n')

        elif search == '2':
            print('찾는 책의 ISBN을 입력해주세요.')
            search = str(input())
            for book in books.keys():
                if book == search:
                    print(books[search])           
                    break                
                else:
                    print('일치하는 책이 없습니다\n')

        elif search == '3':
            print('찾는 책의 저자를 입력해주세요.')
            search = str(input())
            for book in books.values():
                if book.get_author() == search:
                    print(book)
                    found = True
            if not found:    
                print('일치하는 책이 없습니다\n')

        elif search == '4':
            return
        else:
            print('알맞는 번호를 입력해주세요\n')

def deco_line(callback):
    def wrapper(*args):
        print("="*22)
        callback(*args)
        print("="*22)
    return wrapper

@deco_line
def hello(str):
    print(str)