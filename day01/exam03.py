#논리값(True, False) 사용
print(True, False)
print(10 > 3)
print(10 == 3)
print(10 != 3)
print("Hello" == "Hello")
print("Hello" == "hello")
print(1 == 1.0) #== 은 값만 비교하는거라 True가 나옴
print(1 is 1.0) #is는 값만 비교하는게 아니라 완전히 일치하는지 주소값을 비교하는거라 False가 나옴

#주소값에 대한 예제 (id()를 사용하여 해당 값에 주소값을 확인)
print(id('Hello'))
print(id('Hello'))
print(id('hello'))
print(id(1))
print(id(1.0))

print(type(bool(int(str(10))))), bool(int(str(10)))
print(bool(1), bool(0), bool(1.5), bool('fales'))
msg = "hello" and "안녕" #hello를 보고 and를 사용하여 그리고 를 사용하여 안녕을 필수적으로 보기때문에 안녕이 출력
msg = "hello" or "안녕" #hello를 보고 or를 사용하여 또는 을 사용하기 때문에 뒤는 보지 않고 hello를 출력
print(msg)

print('Hello')
print('''Hello''')
print("""Hello
여러줄도 가능
또 라인변경""")

#'''주석''' 의 용도로 쓰려면 맨 위에서만 사용할 수 있음 아래에서 사용하면 문자열의 형태로 사용