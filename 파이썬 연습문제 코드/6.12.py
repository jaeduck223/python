#사용자로부터 n을 입력 받음.
n = int(input('몇 개의 수를 입력하시겠습니까? '))

# 입력받은 수 만큼 사용자로부터 수를 입력받게 함.
#그리고, 입력받은 수 만큼의 수를 리스트 형태로 변환함.
n_list = list(map(int, input(f'{n}개의 수를 입력하세요 : ').split()))

# 결과 출력
print('합 :', sum(n_list))
print('평균 :', sum(n_list) / len(n_list))
print('최댓값 :', max(n_list))
print('최솟값 :', min(n_list))
