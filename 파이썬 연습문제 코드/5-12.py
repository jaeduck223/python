#사용자로부터 밑변과 높이를 입력받음
width = int(input('밑변을 입력하세요 : '))
height = int(input('높이를 입력하세요 : '))

#삼각형의 넓이를 구하는 사용자 정의 함수
def cal_area(width, height):
    return width * height * (1/2)

#결과를 출력한다.
print('삼각형의 면적 : ', cal_area(width, height))
