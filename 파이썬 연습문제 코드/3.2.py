name = input('이름을 입력하시오 : ') # 이름 사용자 입력
height = int(input('키를 입력하시오(단위 cm) : ')) # 키 사용자 입력

# 조건문 : 170 미만이면 탈수 없고, 이상이면 탑승 가능.
if height < 170:
    print(name, '님은 놀이기구를 탈 수 없습니다.')
else:
    print(name, '님은 놀이기구를 탈 수 있습니다.')
