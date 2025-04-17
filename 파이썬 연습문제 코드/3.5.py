# 두 정수를 입력 받아서 작은 수부터 나열하는 프로그램
# split을 이용하여 두 수를 입력 받음.
a, b = input('두 수를 입력하시오 : ').split() # a,b는 문자열

#if-else 구문을 이용하여 출력
if a > b:
    print(b, a)
else:
    print(a, b)
