a, b, c = map(int, input("세 정수를 입력하시오: ").split())

def mean3(a, b, c):
    print(a, b, c, '의 평균값은 :', (a+b+c)/3)
    
mean3(a, b, c)

def min3(a, b, c):
    if (a < b < c) or (a < c < b):
        print(a, b, c, '의 최솟값은 :', a)
    elif (b < a < c) or (b < c < a):
        print(a, b, c, '의 최솟값은 :', b)
    else:
        print(a, b, c, '의 최솟값은 :', c)

min3(a, b, c)

def max3(a, b, c):
    if (c < b < a) or (b < c < a):
        print(a, b, c, '의 최댓값은 :', a)
    elif (c < a < b) or (a < c < b):
        print(a, b, c, '의 최댓값은 :', b)
    else:
        print(a, b, c, '의 최댓값은 :', c)

max3(a, b, c)
