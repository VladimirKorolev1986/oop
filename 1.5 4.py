import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


classes = [Ellipse, Rect, Line]
x = random.choice(classes)
elements = []
for i in range(0, 217):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)
    elements.append(x(a, b, c, d))

for i in elements:
    if isinstance(i, Line):
        i.ep = (0, 0)
        i.sp = (0, 0)
