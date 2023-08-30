class Car:

    addr = '서울'

    __slots__ = ['name', 'price', 'company']

    def __init__(self, **args):
        if 'name' in args:
            self.name = args['name']
        if 'price' in args:
            self.price = args.get('price')
        if 'company' in args:
            self.company = args.get('company')
            Car.addr = '부산'

    def info(self) :
        print(f'자동차명 : {self.name}  가격: {self.price}' )

c = Car(name='그랜저', price=4000, company='현대')
c2 = Car(name='모닝', price=2100)
c.info()
c2.info()
print(c.addr)
print(c2.addr)
