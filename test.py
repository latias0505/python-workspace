str = input('입력:')
str2 = ''
for i in str:
    if i.islower:
        str2 += i.upper()
    else:
        str2 += i.lower()
print(str2)

str = input('입력:')
str2 = ''
for i in str:
    if i.islower():
        str2 += i.upper()
    else:
        str2 += i.lower()
print(str2)
