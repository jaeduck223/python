year = int(input('연도를 입력하세요  : '))
is_leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print(year, '년은 윤년입니까?', is_leap_year)
