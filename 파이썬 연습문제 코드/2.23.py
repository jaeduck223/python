n = int(input('세 자리 정수를 입력하세요 : ')) #사용자 입력

print('백의 자리 : ', n // 100) # // 연산자는 몫을 구하는 연산자!
print('십의 자리 : ', (n % 100) // 10)# % 연산자는 나머지를 구하는 연산자!
print('일의 자리 : ', ((n % 100)) % 10)
