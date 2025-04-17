game_score = int(input('게임점수를 입력하세요 : ')) # 사용자 게임점수 입력

#if-else 구문을 이용해 고수 or 입문자를 판단
if game_score >= 1000:
    print('고수입니다.')
else:
    print('입문자입니다.')
