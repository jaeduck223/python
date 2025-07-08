#사용자로부터 3개의 정수를 입력받아
#오름차순으로 리스트를 출력하는 사용자 정의 함수
def sort3(num1, num2, num3):
    sort2 = []
    sort2.append(num1)
    sort2.append(num2)
    sort2.append(num3)
    sort2.sort()
    return sort2

#사용자로부터 정수 3개를 입력 받음.(소수는 안 되려나....? -> 안된다!)
num1, num2, num3 = map(int, input("세 정수를 입력하세요 : ").split())
sorted_list = sort3(num1, num2, num3)

#결과 출력 사용자 정의 함수 코딩 때, 함수 이름과 리스트 이름 설정 부분에서 헤맴
print('정렬된 리스트는 다음과 같습니다 :', sorted_list[0], sorted_list[1], sorted_list[2])

