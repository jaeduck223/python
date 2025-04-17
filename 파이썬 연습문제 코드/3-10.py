#map,split을 이용하여 두 정수를 입력받음.
a, b = map(int, input("두 정수를 입력하세요 : ").split())
#if-else 구문을 이용해 배수를 판정.
if a % b == 0:
    print(a,'는(은)', b,'의 배수입니다.')
else:
    print(a,'는(은)', b,'의 배수가 아닙니다.')
