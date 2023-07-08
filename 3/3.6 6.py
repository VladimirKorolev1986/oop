import re, sys


class ShopItem:
    def __init__(self, name: str, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = {}
for str_in in lst_in:

    groups = re.search(r'^([^:]+):\s+([\d\.]+)\s+([\d\.]+)\s*$', str_in).groups()
    item = ShopItem(groups[0], groups[1], groups[2])
    total = 1
    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, total]
