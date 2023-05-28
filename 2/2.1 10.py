import random
import string


class EmailValidator:
    STR = string.ascii_letters + string.digits + '@._'

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True

    @classmethod
    def get_random_email(cls):
        """для генерации случайного email-адреса по формату:
        xxxxxxx...xxx@gmail.com,
        где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);"""
        dom = '@gmail.com'
        s = ''
        for _ in range(random.randint(1, 10)):
            s += random.choice(cls.STR)

        return s + dom

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.STR):
            return False
        if len(email[:email.find('@')]) > 100:
            return False
        if len(email[email.find('@'):]) > 50:
            return False
        if '.' not in email[email.find('@'):]:
            return False
        for i in range(len(email) - 1):
            if email[i] == '.' and email[i + 1] == '.':
                return False
        return True


# res = EmailValidator.check_email("sc_lib@list.ru")  # True
res = EmailValidator.check_email("sc_lib@list_ru")  # False

print(res)
