class Viber:
    lst = []

    @classmethod
    def add_message(cls, msg):
        '''добавление нового сообщения в список сообщений'''
        cls.lst.append(msg.text)

    @classmethod
    def remove_message(cls, msg):
        '''удаление сообщения из списк'''
        cls.lst.remove(msg.text)

    @classmethod
    def set_like(cls, msg):
        '''поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
        если лайка нет то он ставится, если уже есть, то убирается)'''
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, n):
        '''отображение последних сообщений'''
        for i in cls.lst[-n:][::-1]:
            print(i)

    @classmethod
    def total_messages(cls):
        '''возвращает общее число сообщений'''
        return len(cls.lst)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like