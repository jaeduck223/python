#메뉴 설명 부분
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('1) 햄버거')
print('2) 치킨')
print('3) 피자')

#while 반복문
#예외처리 : 무한반복문 구조이기에 예외를 처리하여 해당 값이 들어올 때만 if문 동작
#제일 애 먹었던 부분. 검색을 통하여 해결함!
while True:
    try:
        a = int(input('1에서 3까지의 메뉴를 입력하세요: '))

        if a == 1:
            print('햄버거를 선택하였습니다.')
            break
        elif a == 2:
            print('치킨을 선택하였습니다.')
            break
        elif a == 3:
            print('피자를 선택하였습니다.')
            break
        else:
            print('메뉴를 다시 입력하세요.')
    except ValueError:
        print('숫자를 입력하세요.')

