#리스트 선언
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]
#이중 for 문을 이용해 리스트 내의 원소들을 순환하여 곱을 실행함.
for i in list1:
    for j in list2:
        print('{}*{} = {}'.format(i,j,i*j))
