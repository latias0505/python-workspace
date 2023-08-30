'''
    input.txt 읽어 다음의 결과를 출력하시오
    1. 총 단어의 개수 세어보기
    2. 단어의 빈도수 (알파벳순으로 출력)
        ex)
        a       15
        above   1
    3. 단어가 몇번째 라인에 나왔는지 출력
        ex)
        a   15      2, 3, 5, 11, 11, 20
'''

# 문자열 읽어오기
file = open('input.txt', 'r')
data = file.read()
file.close()

# 총 단어의 개수 세기
num1 = len(data)

# 특정 단어의 빈도수 세기
num2 = data.count('so')

print(f'읽어온 데이터 : {data}')
print(num1)