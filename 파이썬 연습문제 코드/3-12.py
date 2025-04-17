x, y = map(int, input("점의 좌표 x,y를 입력하시오: ").split())

if ((x*x) + (y*y)) ** (1/2) >10:
    print('원의 외부에 있습니다.')
else:
    print('원의 내부에 있습니다.')
