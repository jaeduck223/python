#4월7일 수업을 들어야 풀 수 있었던 문제
import math

#최소 공배수를 구하는 사용자 정의 함수
def mini(x, y):
    return x * y // math.gcd(x, y)

#범위 내에서 실시하게끔 하는 사용자 정의 함수
def minimum2(a, b):
    result = a
    for i in range(a + 1, b + 1):
        result = mini(result, i)
    return result

# 사용자 입력
a = int(input("범위의 시작 정수 : "))
b = int(input("범위의 마지막 정수 : "))

#조건문을 통하여 a < b인 경우에만 동작하게 함.
if a < b:
    print(f"{a}부터 {b}까지의 모든 정수의 최소공배수는: {minimum2(a, b)}")
else:
    print("다시 입력해라!!")
