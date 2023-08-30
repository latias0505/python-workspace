data = set([1, 2, 3, 4])
data2 = {1, 4, 5, 6}
print(type(data), data)
print(type(data2), data2)

print(f'합집합(data, data2) : {data.union(data2)}') #union함수는 데이터를 서로 합칠 때 사용 ex) data2에 내용을 data에 합쳐줘
print(f'합집합(data, data2) : {data | data2}')
print(f'교집합(data, data2) : {data.intersection(data2)}') #intersection함수는 서로의 데이터 중 겹치는 데이터를 알고싶을 때 사용
print(f'교집합(data, data2) : {data & data2}')
print(f'차집합(data, data2) : {data.difference(data2)}') #difference함수는 괄호안에 함수의 값 중 앞 함수의 값에 포함되지 않는 값을 알고싶을 때 사용
print(f'차집합(data, data2) : {data2.difference(data)}')  # ex) data에 있는 값 중 data2에 포함되지 않는 숫자를 보이는 코드
print(f'차집합(data, data2) : {data - data2}')
print(f'차집합(data, data2) : {data2 - data}')
print(f'대칭차집합(data, data2) : {data.symmetric_difference(data2)}') #symmetric_difference함수는 서로의 값들 중 겹치지 않는 모든 값을 전부 보여주는 코드
print(f'대칭차집합(data, data2) : {data ^ data2}')

print(data, data2)