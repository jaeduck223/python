#피보나치 수를 출력하는 사용자 정의 함수
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
#사용자로부터 수 입력 받음
nterms = int(input('몇 개의 피보나치수를 원하세요 ?? '))

#조건문을 통해 출력 형태를 지정
if nterms < 0:
    print('오류 : 양수를 입력하시오 : ')
else:
    print('Fibonacci 수열 : ', end = '')
    for n in range(-1, nterms+1):
        print('fibo({:3d} = {:6d})'.format(n, fibonacci(n)))
