score = int(input('점수를 입력하세요 : '))

if score >= 90:
    grade = 'a'
elif score >= 80:
    grade = 'b'
elif score >= 70:
    grade = 'c'
elif score >= 60:
    grade = 'd'
else:
    grade = 'f'

print('당신의 등급은 : ', grade)
