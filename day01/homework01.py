import random

num = int(random.randint(20,50))
print(f'추출된 난수 : {num}')


print('< 369게임 시작!!!>')
for i in range(1, num+1):
    n1 = i % 10
    n10 = i // 10


    print(f'{i:<3}', end=' ') # i:<3을 사용한 이유는 포멧팅을 할 때 자리수를 3개의 자리를 잡고 왼쪽정렬을 한다는 의미 부등호가 반대면 오른쪽 정렬
    if not n1:
        print('뽀'*n10, '숑', end='', sep='')
    if n1 in [3, 6, 9]:
        print('짝', end='')
    if n10 in [3, 6, 9]:
        print('짝', end='')
    print()


"""
r = int(random.randint(20,50))

for i in range(1, r+1):

    count = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if count > 0 and i % 10 != 0:
        print('짝' * count)

    elif i % 10 == 0:
        if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
            print('뽀' * (i // 10) + '숑' + '짝')
        else:
            print('뽀' * (i // 10) + '숑')

    else:
        print(i)
"""