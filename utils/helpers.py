from models.specialized_books import Paper_book, E_book
from datetime import datetime

def register_book(books,isbns):
    hello('신규 도서 등록 메뉴 입니다. 각 항목을 입력해주세요')
    print('책 이름: ')
    while True:
        title = input().strip()
        if not title:
            print("책 이름을 입력해주세요")
        else:
            break
    print('저자: ')
    while True:
        author = input().strip()
        if not author:
            print("저자를 입력해주세요")
        else:
            break
    print('ISBN: ')
    while True:
        isbn = input().strip()
        if isbn in books:
            print('중복된 ISBN 입니다.')
        elif not isbn:
            print('ISBN을 입력해주세요')
        else:
            break
    print('책 타입 (일반 or 전자):')
    while True:
        type = input().strip()
        if type in ['일반','전자']:
            if type == '일반':
                ebook = False
            else:
                ebook = True
            break
        else:
            print('일반 혹은 전자로 입력해주세요')
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
    while True:
        found = False
        hello('책의 검색 방법을 입력해주세요.')
        print('1. 책 제목')
        print('2. ISBN')
        print('3. 저자')
        print('4. 메인으로')
        search = input()

        if search == '1':
            print('찾는 책의 제목을 입력해주세요.')
            search = input()
            for book in books.values():
                if book.get_title() == search:
                    print(book)                     # book 객체기 때문에 __str__ 이 작동
                    found = True
            if not found:    
                print('일치하는 책이 없습니다\n')

        elif search == '2':
            print('찾는 책의 ISBN을 입력해주세요.')
            search = input()
            if search in books:
                print(books[search])          
                                
            else:
                print('일치하는 책이 없습니다\n')

        elif search == '3':
            print('찾는 책의 저자를 입력해주세요.')
            search = input()
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

def borrow(books,statistics):
    while True:
        hello('도서 대여/반납 메뉴 입니다')
        print('1. 대여 도서 목록 검색')
        print('2. 도서 대여')
        print('3. 도서 반납')
        print('4. 메인으로')
        menu = input()

        if menu == '1':
            for book in books.values():
                if book.get_borrowed():
                    print(book)

        elif menu == '2':
            while True:
                print('대여할 도서의 ISBN을 입력하세요')
                isbn = input()
                if isbn in books:
                    book = books[isbn]
                    if book.borrow():
                        print('도서가 대여 되었습니다')
                        statistics.append(isbn,datetime.now(),'대여')
                        break                    
                    else:
                        print('대여중인 도서 입니다')
                else:
                    print('ISBN이 일치하는 도서가 없습니다')
                    break

        elif menu == '3':
            while True:
                print('반납할 도서의 ISBN을 입력하세요')
                isbn = input()
                if isbn in books:
                    book = books[isbn]
                    if book.return_book():
                        print('도서가 반납 되었습니다')
                        statistics.append((isbn,datetime.now(),'대여'))
                        break
                    else:
                        print('대여중인 도서가 아닙니다')
                else:
                    print('ISBN이 일치하는 도서가 없습니다')
                    break

        elif menu == '4':
            return
        else:
            print('알맞은 번호를 입력해주세요\n')

def book_static(books,statistics):
    while True:
        hello('통계 조회 메뉴입니다')
        print('1. 가장 많이 대여된 도서')
        print('2. 월간 대여 통계')
        print('3. 메인으로')
        count = {}
        menu = input()
        if menu == 1:
            for isbn, time, borrow in statistics:
                if borrow == '대여':
                    count[isbn] = 
            
