#리스트가 주어짐.
a = [2, 3, 4, 5, 6]
print('a =', a)
#빈 리스트를 만듦.
rev_a = []

# 반복문과 팝 메소드를 이용하여 리스트의 순서를 바꿈
for i in range(len(a)):
    rev_a.append(a.pop())

# 결과 출력
print('rev_a =', rev_a)
