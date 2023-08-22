num = int(input('정수 입력 : '))
if num > 0 :
    if num % 2:
        print(num, ': 홀수') #num을 2로 나눠서 참인 경우는 1인 경우이므로 홀수
    else:
        print(num, ': 짝수') #num을 2로 나눠서 거짓인 경우는 0인 경우이므로 짝수
else:
    print('짝/홀 판단은 양수만 가능합니다.')

if num < 0:
    print('짝/홀 판단은 양수만 가능')
elif num % 2:
    print(num, ': 홀수')
else:
    print(num, ': 짝수')

"""
import random

r = int(random.random() * 10) #랜덤으로 숫자 10개를 추출하여 생성

if r % 2 == 0:
    print(f'{r} : 짝수')
else:
    print(f'{r} : 홀수')
"""