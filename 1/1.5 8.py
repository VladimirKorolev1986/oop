class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        lst = []
        for i in self.goods:
            lst.append(f'{i.name}: {i.price}')


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
tv1 = TV('Samsung', 1000)
tv2 = TV('Sony', 700)
tabl = Table('Dad', 5000)
note1 = Notebook('MSY', 10000)
note2 = Notebook('Sony', 5000)
cup = Cup('Beer', 50)

cart.add(tv1)
cart.add(tv2)
cart.add(tabl)
cart.add(note1)
cart.add(note2)
cart.add(cup)


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price
