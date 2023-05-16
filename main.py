class Server:
    ip = 0

    def __init__(self):
        self.ip += 1
        Server.ip = self.ip


class Router:

    @classmethod
    def link(cls):
        """для присоединения сервера server (объекта класса Server)
        к роутеру (для простоты, каждый сервер соединен только с одним роутером"""
        pass

    @classmethod
    def link(cls):
        """для отсоединения сервера server (объекта класса Server) от роутера"""
        pass


class Data:
    pass


sv0 = Server()
sv1 = Server()
sv2 = Server()
