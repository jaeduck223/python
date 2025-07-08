#섭씨온도를 화씨온도로 변환하는 사용자 정의 함수
def cel2fah(cel):
    return cel * (9/5) + 32
#FOR 문을 이용하여 출력한다아아
for cel in range(10, 101, 10):
    print('섭씨 ', cel, '도 = 화씨 ', cel2fah(cel), '도 입니다.')
