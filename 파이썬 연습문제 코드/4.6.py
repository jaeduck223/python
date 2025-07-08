#사용자 입력 
n = int(input('숫자를 입력하세요: '))

# for 문을 이용하여 별 패턴을 형성함.
for i in range(1, n + 1):
    # 공백 출력
    for j in range(n - i):
        print(' ', end='')
    # 별 출력
    for k in range(i):
        print('*', end='')
    print()  # 줄 바꿈

