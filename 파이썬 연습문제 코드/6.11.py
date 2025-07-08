#사용자로부터 숫자 5개를 입력받음.
a, b, c, d, e = map(int, input('5개의 수를 입력하세요 : ').split())

#리스트 형성
n_list = [a, b, c, d, e]

#결과 출력 -> 리스트의 내장함수를 이용하여 결과를 출력.
print('합 : ', sum(n_list))
print('평균 : ', sum(n_list)/len(n_list))
print('최댓값 :', max(n_list))
print('최솟값 :', min(n_list))
