class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y


lst = []
for i in range(1, 1999, 2):
    print(i)
    if i == 3:
        lst.append(Point(i, i, 'yellow'))
    lst.append(Point(i, i))
