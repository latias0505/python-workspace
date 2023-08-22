# 방법1 = 일반적으로 입력값을 입력받는 방법
'''
num01 = input('첫번째 정수 입력 : ')
num02 = input('두번째 정수 입력 : ')
print(num01, num02)
'''

#방법2 = 한번에 두개의 정수를 입력받는 방법
print(type('12, 5'.split())) #split을 사용하여 자르면 리스트 배열의 형태로 저장됨

#map(int, input())의 형태로 map을 사용하면 입력받는 input값이 int형으로 저장됨
num01, num02 = map(int, input('두개의 정수를 입력 : ').split()) #입력받은 두개의 정수를 split()을 사용하여 분리해서 num01 num02 순서에 대응하여 0분지 1분지 순서대로 저장
print(type(num01), type(num02))
