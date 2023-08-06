import sys, re


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))


str = "Системный блок: 1500 75890.56"

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = list(map(str.strip, str))

shop_items = {}
for i in lst_in:
    text = i.split()
    text[-3] = text[-3].replace(':', '')
    item = ShopItem(' '.join(text[0:-2]), float(text[-2]), float(text[-1]))
    total = 1
    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, total]

print(lst_in)

p1 = ShopItem('Samsung', 10, 2000)
p2 = ShopItem('Samsung', 10, 2000)

print(p1 == p2)
print(hash(p1))
print(hash(p2))
