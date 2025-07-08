#코드는 아래와 같이 사용자의 입력을 받는 것으로 시작한다.
x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

#두 점의 거리를 구하는 사용자 정의 함수
def distance(x1,y1,x2,y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

print('두 점의 거리 : ', distance(x1,y1,x2,y2))
