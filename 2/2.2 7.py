class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if type(x) in (float, int) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x
        if type(y) in (float, int) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (float, int) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (float, int) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y
