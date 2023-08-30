# quit가 나올때까지 문자열을 입력받아 test02.txt 저장
# test02.txt에 저장된 모든 문자열을 읽어서 모니터에 출력

# with open('test02.text', 'w') as file:
#     print('문자열들을 입력하세요. quit 입력시 종료')
#     while True :
#         msg = input()
#         if msg == 'quit':
#             break
#         file.write(f'{msg}\n')
#         #file.write('{0}\n'.format(msg))
#
# print('파일 저장 완료...')

# with open('test02.text', 'r') as file:
#     lines = file.readlines()
#
# print('< 읽어온 데이터 출력 >')
# for line in lines:
#     print(line.rstrip('\n'))
