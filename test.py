class PhoneNumber:
    def __init__(self, number=0, fio=''):
        self.__number = number
        self.__fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, int) and len(str(number)) == 11:
            self.__number = number


a = PhoneNumber(2323, "Vl")
b = PhoneNumber(2322223, "Vl")

