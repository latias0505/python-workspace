num = 1
while num <= 10: #num이 10과 같거나 작아질때까지 동작
    print(num, end=' ')
    num += 1 #num값을 1씩 증가시킴
print()

for i in range(10): #
    print(i+1, end=' ')
print()

for i in range(10):
    if (i+1) % 2:
        print(i+1, end=' ')
print()

for i in range(0, 10, 2):
    print(i+1, end=' ')
print()

names = ['홍길동', '강길동', '윤길동']
for name in names:
    print(name, end=' ')
print()

for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(5):
    print('*' * (i+1))

for i in range(9):
   if i < 5:
       print('*' * (i+1))
   else:
       print('*' * (9-i))

for i in range(9):
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)