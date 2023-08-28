data = {'hong': 1111, 'kang': 2222, 'han': 3333, 'park': 4444, 'kang': 5555}
print(data, type(data))

stuInfo = {'name': 'hong', 'age':28, 'scores': [100, 100, 70]}
print(stuInfo)

data = {}
data = dict()
data = dict(name='hong', age=28, addr='seoul')
data = dict([('name', 'hong'), ('age', 28), ('addr', 'seoul'), ('1', '')])
data = dict(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))
print(data, type(data))
print(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))