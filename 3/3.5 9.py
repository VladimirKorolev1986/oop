class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def weight(self):
        return self.ro * self.volume

    def __gt__(self, other):
        if isinstance(other, Body):
            return self.weight() > other.weight()
        return int(self.weight()) > other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.weight() < other.weight()
        return int(self.weight()) < other

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.weight() == other.weight()
        return self.weight() == other


body1 = Body('Bag', 3, 2)
body2 = Body('Bag1', 4, 2)

print(body1 > body2 ) # True, если масса тела body1 больше массы тела body2
print(body1 < body2 ) # True, если масса тела body1 больше массы тела body2
print(body1 == body2)  # True, если масса тела body1 равна массе тела body2
print(body1 < 10)  # True, если масса тела body1 меньше 10
print(body2 == 5)  # True, если масса тела body2 равна 5
print("Yes")