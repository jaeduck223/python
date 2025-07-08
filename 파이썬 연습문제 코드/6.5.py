#리스트 선언
list1 = ['I like', 'I love']
list2 = ['fan cake.', 'kiwi juice.', 'espresso.']
#이중 for문을 이용하여 각 원소들을 순회한 다음
#포맷팅을 이용하여 지정된 위치에 출력함.
for i in list1:
    for j in list2:
        print('{} {}'.format(i,j))
