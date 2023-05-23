class AppStore:
    storage = []

    @classmethod
    def add_application(cls, app):
        """добавление нового приложения app в магазин"""
        cls.storage.append(app)

    @classmethod
    def remove_application(cls, app):
        """удаление приложения app из магазина;"""
        cls.storage.remove(app)

    def block_application(self, app):
        """блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);"""
        app.blocked = True

    @classmethod
    def total_apps(cls):
        """возвращает общее число приложений в магазине"""
        return len(cls.storage)


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False



