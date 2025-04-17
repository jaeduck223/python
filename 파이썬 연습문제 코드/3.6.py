#map은 모든 자료형에 대하여 함수를 적용할 수 있다
a, b, c = map(int, input("세 정수를 입력하시오: ").split())

# 여러가지 경우를 고려하기 위해 if-elif-else 구문 사용.
if a > b > c:
    print(c, b, a)
elif a > c > b:
    print(b, c, a)
elif b > a > c:
    print(c, a, b)
elif b > c > a:
    print(a, c, b)
elif c > a > b:
    print(b, a, c)
else:
    print(a, b, c)
