data = list(range(1, 10))
print(data)

data2 = data[0:5] #슬라이스를 이용해서 data 값에 0번지부터 5번지 전 까지를 잘라내서 data2에 넣음
print(data)
print(data2)
print(data[5:8]) #슬라이스를 이용해서 data의 값 중 5번지부터 8번지 전 까지만 잘라내서 출력
print(data[:3]) #시작 값을 입력하지 않아 디폴트로 data에 처음 숫자부터 슬라이스로 3까지의 숫자만 잘라내서 출력
print(data[3:]) #끝 값을 입력하지 않아 data 값에 3번지부터 끝까지 출력     print(data[3:len(data)])와 같음
print(data[:])
print('--------------------------------------')
print(data)
#data2 = data
data2 = data[:]
print(data2)
data2[0] = 100
print('data:', data, id(data))
print('data', data, id(data2))

print(data[5:len(data)])
print(data[5:-1])
print(data[8:2:-2])
print(data[::-1]) #::을 사용하여 끝에서부터 처음 숫자까지 -1씩 차감하여 나열

print('data:', data)

#data[2:5] = [100, 200, 300]
#data[2:5] = [100]
#data[2:5] = [100, 200, 300, 400, 500]
data[2:6:2] = [10, 20] #2분지부터 시작해서 6분지 전까지의 숫자에서 2를 포함하여 2씩 증가하는 숫자를 각각 10과 20으로 변경
print('data', data)

#del data[2:3]
del data[2:5]
print('data:', data)