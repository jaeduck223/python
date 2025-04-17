#map,split을 이용하여 x,y좌표를 입력 받음!
x, y = map(int, input("점의 좌표 x, y를 입력하시오: ").split())
#if-elif-else구문과 복합 조건식을 이용해 사분면을 판정함.
if x > 0 and y > 0:
    print("1사분면에 있어요.")
elif x < 0 and y > 0:
    print("2사분면에 있어요.")
elif x < 0 and y < 0:
    print("3사분면에 있어요.")
else:
    print("4사분면에 있어요.")
