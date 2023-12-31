members = {'홍길동': '1111-2222', '박길동': '3333-4444', '윤길동': '5555-6666'}

print(f'홍길동 존재여부 : {"홍길동" in members}')
print(f'고길동 존재여부 : {"고길동" in members}')

print(members.keys())
print(members.values())
print(members.items())

for data in members:
    #print(data, end=' ')
    print(f'{data} : {members.get(data)}')
print()

for data in members.keys():
    print(data, end=' ')
print()

for data in members.values():
    print(data, end=' ')
print()

nums = [2, 3, 6]
a, b, c = nums
print(f'a:{a}, b:{b}')

for key, value in members.items():
    print(f'{key} : {value}')

keys = ['name', 'age', 'addr']
mem = dict.fromkeys(keys, "")
print(mem)
