#무려 6개나 사용자로부터 입력 받음!
a, b, c, d, e, f = map(int, input('여섯 개의 정수를 입력하세요 : ').split())

#평균값을 구하는 사용자 정의 함수
def mean6(a, b, c, d, e, f):
    return (a+b+c+d+e+f) / 6

#4.9일 수업에서 배운 내장함수 max를 이용하여 최댓값을 구하는 사용자 정의 함수
def max6(a, b, c, d, e, f):
    return max(a, b, c, d, e, f)

#4.9일 수업에서 배운 내장함수 min을 이용하여 최솟값을 구하는 사용자 정의 함수
def min6(a, b, c, d, e, f):
    return min(a, b, c, d, e, f)

#결과를 출력한다!!!!
print('평균값은 ', mean6(a, b, c, d, e, f))
print('최댓값은 ', max6(a, b, c, d, e, f))
print('최솟값은 ', min6(a, b, c, d, e, f))
