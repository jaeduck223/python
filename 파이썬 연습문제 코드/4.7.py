n = int(input('숫자를 입력하세요 : '))

for num in range(2, n):
    
    if n % num == 0:
        is_prime = False
        print(n,'는 소수입니다.' )
    else:
        print(n,'는 소수가 아닙니다.')
