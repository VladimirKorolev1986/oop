from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    def __init__(self):
        pass

    @staticmethod
    def check_card_number(number: str):
        """Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - лю бая цифра (от 0 до 9)."""
        if len(number.split('-')) != 4:
            return False
        if not any([x.isdigit() for x in number.split('-')]):
            return False
        for x in number.split('-'):
            if len(x) != 4:
                return False
        return True

    @classmethod
    def check_name(cls, name):
        """Формат имени:
        два слова (имя и фамилия) через пробел,
        записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV SDS."""
        if len(name.split()) != 2:
            return False
        if set(name.split()[1]) > set(cls.CHARS_FOR_NAME) and set(name.split()[2]) > set(cls.CHARS_FOR_NAME):
            return False
        return True


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number)
print(is_name)
