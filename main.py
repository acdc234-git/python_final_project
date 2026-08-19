from models.specialized_books import Paper_book, E_book
#from utils.helpers import register_book, show_book
import utils.helpers as util

def main():
    books = {}      # 딕셔너리 구조로 isbn : book 으로 구성하여 유일한 값인 isbn으로 책의 값들을 관리 할 수 있다.
    isbns = set()   # set()을 사용해 isbn을 유일한 값으로 관리한다.
    statistics = ()

    book1 = Paper_book('책1', '저자1', '1111')  # 테스트 데이터
    book2 = Paper_book('책2', '저자2', '2222')
    book3 = E_book('책1', '저자1', '3333')
    book4 = E_book('책2', '저자2', '4444')
    books['1111'] = book1
    books['2222'] = book2
    books['3333'] = book3
    books['4444'] = book4                      
    isbns = set(books)                          # 테스트 데이터
    while True:
        util.hello('='*3 + '도서 관리 시스템' + '='*3)
        print("1. 도서 등록")
        print("2. 전체 도서 조회")
        print("3. 도서 검색")
        print("4. 대여/반납 처리")
        print("5. 통계 조회")
        print("6. 종료")

        try:
            num = int(input())

            if num == 1:
                util.register_book(books,isbns)     
            elif num == 2:
                util.show_book(books)
            elif num == 3:
                util.search_book(books)       
            elif num == 4:
                util.borrow(books,statistics)        
            elif num == 5:
                pass
            elif num == 6:
                break
            else:
                print("알맞는 번호를 입력해주세요\n")

        except ValueError:
            print('숫자를 입력해주세요')

if __name__ == "__main__":
    main()