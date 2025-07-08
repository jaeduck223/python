#사용자 숫자 입력
n = int(input('숫자를 입력하세요 : ' ))
s = 0
#for 문을 통한 제곱의 합산 구하는 프로그램
for i in range(1, n+1):
    s = s + (i ** 2)

print('결과는', s, '입니다.')
