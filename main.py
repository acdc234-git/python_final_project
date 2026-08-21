from models.specialized_books import Paper_book, E_book
#from utils.helpers import register_book, show_book
import utils.helpers as util
import pickle

def main():    
    try:
     with open('libarary.pkl','rb') as fp:
        libarary_data = pickle.load(fp)
        books = libarary_data['books']
        record = libarary_data['record']
    except FileNotFoundError:
        books = {} # 딕셔너리 구조로 isbn : book 으로 구성하여 유일한 값인 isbn으로 책의 값들을 관리 할 수 있다.
        record = []  # 통계 조회를 위한 대여 기록
    
    while True:
        util.hello('='*3 + '도서 관리 시스템' + '='*3)
        print("1. 도서 등록")
        print("2. 전체 도서 조회")
        print("3. 도서 검색")
        print("4. 대여/반납 처리")
        print("5. 통계 조회")
        print("6. 종료")

        try:
            num = int(input('메뉴 번호를 입력하세요: '))

            if num == 1:
                util.register_book(books,record)     
            elif num == 2:
                util.show_book(books)
            elif num == 3:
                util.search_book(books)       
            elif num == 4:
                util.borrow(books,record)        
            elif num == 5:
                util.book_record(books,record)
            elif num == 6:
                break
            else:
                print("알맞는 번호를 입력해주세요\n")

        except ValueError:
            print('숫자를 입력해주세요')

if __name__ == "__main__":
    main()