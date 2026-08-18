from models.specialized_books import Paper_book, E_book
#from utils.helpers import register_book, show_book
import utils.helpers as util

books = {}      # 딕셔너리 구조로 isbn : book 으로 구성하여 유일한 값인 isbn으로 책의 값들을 관리 할 수 있다.
isbns = set()   # set()을 사용해 isbn을 유일한 값으로 관리한다.

book1 = Paper_book('책1', '저자1', '1111')
book2 = Paper_book('책2', '저자2', '2222')
book3 = E_book('책1', '저자1', '3333')
book4 = E_book('책2', '저자2', '4444',True)

books['1111'] = book1
books['2222'] = book2
books['3333'] = book3
books['4444'] = book4

while True:
    util.hello('='*3 + '도서 관리 시스템' + '='*3)
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 대여/반납 처리")
    print("5. 종료")

    num = input()

    if num == '1':
        util.register_book(books,isbns)     
    elif num == '2':
        util.show_book(books)
    elif num == '3':
        util.search_book(books)       
    elif num == '4':
        #메뉴로 가는 코드 입력 필요
        print("")        
    elif num == '5':
        break
    else:
        print("알맞는 번호를 입력해주세요\n")

        