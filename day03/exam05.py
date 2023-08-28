# 패스워드 변경 서비스
members = {'aaa': '111', 'bbb': '222', 'ccc': '333', 'ddd': '444'}

print('패스워드 변경서비스 입니다.')
id = input('아이디를 입력하세요 : ')

if id not in members: # 입력한 아이디가 members 안에 존재하지 않을 때
    print(f'입력하신 아이디[{id}]는 존재하지 않습니다.')
    print('패스워드 변경서비스를 종료합니다.')
    exit(0)

password = input('패스워드를 입력하세요 : ')
if members.get(id) != password:
    print('패스워드가 일치하지 않습니다.')
    print('패스워드 변경서비스를 종료합니다.')
    exit(0)

newPassword = input('변경할 패스워드를 입력하세요 : ')
#members.update(id=newPassword)
members.update([[id, newPassword]])
#members.update({id:newPassword})
#members[id] = newPassword

print('< 전체 회원 목록 >')
print('아이디\t패스워드')
for id, pw in members.items():
    print(f'{id}\t{password}')
print()