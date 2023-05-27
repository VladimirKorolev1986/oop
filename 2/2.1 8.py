class Point:
    def __init__(self, x=0, y=0):
        # if self.__check(x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

    # @classmethod
    # def __check(cls, x, y):
    #     if x in (int, float) and y in (int, float):
    #         return True


class Rectangle:
    def __init__(self, *args):
        if isinstance(args[0], Point) and isinstance(args[0], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp} {self.__ep}")


rect = Rectangle(0, 0, 20, 34)

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep,
                                                          Point), "атрибуты __sp и __ep должны ссылаться на объекты класса Point"
