import random

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