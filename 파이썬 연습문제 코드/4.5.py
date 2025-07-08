#메뉴 설명 부분
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('- 햄버거(입력 b)')
print('- 치킨(입력 c)')
print('- 피자(입력 p)')

#while 반복문
# 4.4와는 문자열이냐 정수이냐의 차이 밖에 없다.
while True:
    try:
        a = input('메뉴를 선택하세요(알파벳 b, c, p 입력) : ')

        if a == 'b':
            print('햄버거를 선택하였습니다.')
            break
        elif a == 'c':
            print('치킨을 선택하였습니다.')
            break
        elif a == 'p':
            print('피자를 선택하였습니다.')
            break
        else:
            print('메뉴를 다시 입력하세요.')
    except ValueError:
        print('메뉴를 다시 입력하세요(알파벳 b, c, p 입력) :')

