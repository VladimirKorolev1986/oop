class PhoneNumber:
    def __init__(self, number, fio):
        if self.valid(number):
            self.__number = number
        if self.valid_fio(fio):
            self.__fio = fio

    # @property
    # def number(self):
    #     return self.__number
    #
    # @number.setter
    # def number(self, number):
    #     if isinstance(number, int) and len(str(number)) == 11:
    #         self.__number = number

    @staticmethod
    def valid(number):
        if isinstance(number, int) and len(str(number)) == 11:
            return True

    @staticmethod
    def valid_fio(fio):
        if isinstance(fio, str):
            return True


class PhoneBook:
    LST = []

    @classmethod
    def add_phone(cls, phone):
        cls.LST.append(phone)

    @classmethod
    def remove_phone(cls, indx):
        cls.LST.pop(indx)

    @classmethod
    def get_phone_list(cls):
        return cls.LST

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()