print('< 읽어온 데이터 >')

# 방법2
with open('test02.text', 'r') as file:

    for line in file:
        print(line.rstrip('\n'))

    # line = file.readline().rstrip('\n')
    # while line != '':
    #     print(line)
    #     line = file.readline().rstrip('\n')

# #방법1
# with open('test02.text', 'r') as file:
#     while True:
#         line = file.readline()
#         if line == '':
#             break
#         print('[{}]'.format(line.rstrip("\n")))
