'''
    open(파일명, 모드)
    read()/write()
    close()

    with open() as 파일객체:
'''
#file = open('test.txt', "w")
#file.write('Hello')
#file.close()

file = open('test.txt', 'r')
data = file.read()
file.close()
print(f'읽어온 데이터 : {data}')