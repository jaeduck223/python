a, b, c = map(int, input("세 복권번호를 입력하시오(1~10) : ").split())

if (a==2) and (b==3) and (c==9):
    print('상금 1만원')
elif (a==2 and b==3) or (b==3 and c==9) or (a==2 and c==9):
    print('상금 1천만원')
elif (a==2 and b==3 and c==9):
    print('상금 1억원')
else:
    print('다음 기회에...메롱')
