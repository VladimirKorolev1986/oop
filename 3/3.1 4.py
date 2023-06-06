class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 1

    def __init__(self, name, weight, price):
        self.id += 1
        Product.id = self.id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'id':
            if type(value) != int:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == "name":
            if type(value) != str:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'weight':
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'price':
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)



