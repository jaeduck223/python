a, b, c = map(int, input("세 정수를 입력하시오: ").split())

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
