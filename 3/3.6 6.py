class ShopItem:
    def __init__(self, name: str, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

new_s = []
for i in lst_in:
    new_s.append(i.split(":"))

print(new_s)

