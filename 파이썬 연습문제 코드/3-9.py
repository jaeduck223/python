n = int(input('정수를 입력하세요 : ')) #사용자로부터 정수 입력

#if-else 구문과 논리 연산자를 이용하여 입력 정수에 대한 2 또는 3의 배수 판정
if n % 2 != 0:
    print(n,'는(은) 2(으)로 나누어지지 않습니다.')
else:
    print(n,'는(은) 2(으)로 나누어집니다.')
    
if n % 3 == 0:
    print(n,'는(은) 3(으)로 나누어집니다.')
else:
    print(n,'는(은) 3(으)로 나누어지지 않습니다.')
    
if (n % 2 == 0) and (n % 3 == 0):
    print(n,'는(은) 2와(과) 3 모두로 나누어집니다.')
else:
    print(n,'는(은) 2와(과) 3 모두로 나누어지지 않습니다.')
