from models.specialized_books import Paper_book, E_book

books = []

while True:
    print("="*22)
    print("="*3+"도서 관리 시스템"+"="*3)
    print("="*22)
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 대여/반납 처리")
    print("5. 종료")

    num = input()

    if num == '1':
        #도서등록 메뉴로 가는 코드 입력 필요
        print('신규 도서 등록 메뉴 입니다. 각 항목을 입력해주세요')
        print('책 이름: ')
        title = str(input())
        print('저자: ')
        author = str(input())
        print('ISBN: ')
        isbn = str(input())
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
        books.append(new_book)
    elif num == '2':
        pass
    elif num == '3':
        #메뉴로 가는 코드 입력 필요
        print("")        
    elif num == '4':
        #메뉴로 가는 코드 입력 필요
        print("")        
    elif num == '5':
        break
    else:
        print("알맞는 번호를 입력해주세요")

        