#마일을 입력받아서 킬로미터로 반환하는 사용자 정의함
def mile2km(m):
    return m * 1.61
#반복문을 이용한 출력
for m in range(1,11):
    print(m, '마일 = ', mile2km(m), '킬로미터')

