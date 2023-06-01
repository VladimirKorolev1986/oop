from math import sqrt


class LineTo:
    LIST = [(0, 0)]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.linked()

    def linked(self):
        self.LIST.append((self.x, self.y))


class PathLines:

    def __init__(self, *args):
        self.line = args

    def get_path(self):
        """возвращает список из объектов класса LineTo (если объектов нет, то пустой список);"""
        if self.line:
            lst = []
            for i in self.line:
                lst.append(i)
            return lst
        return []

    def get_length(self):
        """возвращает суммарную длину пути (сумма длин всех линейных сегментов); L = sqrt((x1-x0)^2 + (y1-y0)^2)"""
        lng = self.get_path()[-1:]
        s = 0
        ll = lng[0].LIST
        for i in range(len(ll) - 1):
            s += sqrt((ll[i + 1][0] - ll[i][0]) ^ 2 + (ll[i + 1][1] - ll[i][1]) ^ 2)
        return s

    def add_line(self, line):
        """добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута."""
        self.get_path().append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
dist = p.get_length()

# a = LineTo(10, 20)
# b = LineTo(10, 30)
# c = LineTo(10, 40)
# d = LineTo(10, 50)
