age = int(input('나이를 입력하시오 : '))

if age >= 20:
    print('Adult')
elif age >= 10 and age < 20:
    print('Youth')
else:
    print('Kid')
