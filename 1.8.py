class Server:
    ip = 0

    def __init__(self):
        self.ip += 1
        Server.ip = self.ip
        self.buffer = {}

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя
        (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);"""

    def get_data(self):
        """возвращает список принятых пакетов
        (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;"""

    def get_ip(self):
        """возвращает свой IP-адрес."""


class Router:
    def __init__(self):
        self.buffer = {}
    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        (для простоты, каждый сервер соединен только с одним роутером);"""
        pass

    def unlink(server):
        """для отсоединения сервера server (объекта класса Server) от роутера;"""
        pass

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data)
        из буфера роутера соответствующим серверам (после отправки буфер должен очищаться)."""
        pass


class Data:
    def __init__(self, data, ip_pur):
        self.data = data
        self.ip_pur = ip_pur
