import math


class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.img = img
        self.real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, val):
        if type(val) in (int, float):
            self.__img = val
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, val):
        if type(val) in (int, float):
            self.__real = val
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return math.sqrt(self.real * self.real + self.img * self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
