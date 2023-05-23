class Viber:
    def add_message(self, msg):
        """добавление нового сообщения в список сообщений;"""

    def remove_message(self, msg):
        """удаление сообщения из списка;"""

    def set_like(self, msg):
        """поставить/убрать лайк для сообщения msg
        (т.е. изменить атрибут fl_like объекта msg:
        если лайка нет то он ставится, если уже есть, то убирается);"""


    def show_last_message(self, number):
        """отображение последних сообщений;"""


class Message:
    def __init__(self):
        self.text = text