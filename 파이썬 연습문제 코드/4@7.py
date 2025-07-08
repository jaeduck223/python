n = int(input("양의 정수를 입력하세요: "))
#if-elif-else 구문 사용하여 문구 작성
if n < 2:
    print(f"{n}는 소수가 아닙니다.")
elif n == 2:
    print(f"{n}는 소수입니다.")  
elif n % 2 == 0:
    print(f"{n}는 소수가 아닙니다.") 
else:
    is_prime = True   # 소수 초기화
    i = 3             #홀수
    while i * i <= n: 
        if n % i == 0:
            is_prime = False
            break
        i += 2        #홀수로 나눗셈 시도하게끔 함.

    if is_prime:    #if-else 구문을 이용하여 결과 출력
        print(f"{n}는 소수입니다.")
    else:
        print(f"{n}는 소수가 아닙니다.")

#역대급으로 어려운 문제. 재수강임에도 아직 어려운 면이 없지 않아 있다.
