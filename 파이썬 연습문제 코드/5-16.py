#제일 어려웠던 문제
#리스트를 형성하여, 오름차순으로 정렬하는 사용자 정의 함수
def sort_numbers(input_str):
    input_list = []
    for i in input_str.split(','): #for 문을 이용하여 리스트에 항목을 추가함.
        input_list.append(int(i))
    
    sorted_list = input_list.copy()
    sorted_list.sort()

    return input_list, sorted_list

#사용자로부터 정수를 입력받음.
input_str = input('쉼표로 구분된 정수를 임의의 개수 입력하시오: ')
original_list, sorted_list = sort_numbers(input_str)

#출력문 -> for 문을 이용하여 정수를 출력함.
print('입력된 정수의 리스트:', original_list)
print('정렬된 정수의 리스트:', end=' ')
for n in sorted_list:
    print(n, end=' ')

#과연 음수에 대해서도 작동할까? ->> 잘 작동한다!!!!!
