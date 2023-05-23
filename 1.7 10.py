class AppStore:
    storage = []
    def add_application(self, app):
        """добавление нового приложения app в магазин"""
        pass

    def remove_application(self, app):
        """удаление приложения app из магазина;"""
        pass

    def block_application(self, app):
        """блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);"""
        pass

    def total_apps(self):
        """возвращает общее число приложений в магазине"""
        pass


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
