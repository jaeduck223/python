import math 

# 사용자로부터 n을 입력 받음
n = int(input('몇 개의 수를 입력하시겠습니까? '))

# 입력받은 수 만큼 사용자로부터 수를 입력받고 리스트로 변환함!
n_list = list(map(int, input(f'{n}개의 수를 입력하세요 : ').split()))

# 표준편차를 구하기 위해 평균을 일단 구함.
mean = sum(n_list) / len(n_list)

# 표준편차 식을 이용하여 표준편차를 구하는 식 완성.
v = sum((x - mean) ** 2 for x in n_list) / len(n_list)
std = math.sqrt(v)

# 결과 출력
print('입력된 수 :', n_list)
print('합 :', sum(n_list))
print('평균 :', mean)
print('표준편차 :', std)
