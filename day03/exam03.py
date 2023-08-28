members = {'홍길동':'010-1111-2222', '박길동':'010-3333-4444'}
print(members)
members.setdefault('윤길동', '010-5555-6666')
members.setdefault('이길동')
print(members)


members.update(이길동='010-7777-8888')
members.update(한길동='010-9999-0000')
members.update({202308501:'010-22345-6789'})
members.update([[2023082502, '010-1234-5678'], ['고길동' '010-4567-8910']])
members.update(zip(['park', '이길동'], ['8282', None]))
print(members)