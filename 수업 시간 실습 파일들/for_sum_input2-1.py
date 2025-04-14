n = -1
while n <= 0:
    n = int(input('합계를 구할 양의 정수를 입력하세요 :' ))
s = 0
for i in range(1, n+1):
    s = s + i
print('1부터 {}까지의 합은 {}'.format(n, s))
