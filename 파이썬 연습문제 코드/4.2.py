#항상 참인 경우에 대하여
while True:
    a = int(input('1에서 9까지의 수를 입력하세요: '))
    #if 조건문 and break 구문
    if 1 <= a <= 9:
        break
    
    print('잘못된 입력입니다. 1에서 9까지의 수를 다시 입력하세요.')
#사용자 입력에 맞춘 구구단 출력하는 이중 while 문.
i = a
while i <= a:
    j = 1
    while j < 10:
        print('{}*{} = {:2d}'.format(i, j, i*j), end=' ')
        j += 1
    print()
    i += 1
