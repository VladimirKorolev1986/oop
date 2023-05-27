class Router:
    def __init__(self):
        self.servers = {}
        self.buffer = []

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        (для простоты, каждый сервер соединен только с одним роутером);"""
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера;"""
        self.servers.pop(server.get_ip())

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data)
        из буфера роутера соответствующим серверам (после отправки буфер должен очищаться)."""
        for i in self.buffer:
            if i.ip_pur in self.servers:
                rout = self.servers[i.ip_pur]
                rout.buffer.append(i)
            else:
                False

        self.buffer = []


class Server:
    ip = 0

    def __init__(self):
        self.ip += 1
        Server.ip = self.ip
        self.buffer = []
        self.router = None

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя
        (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);"""
        self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов
        (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;"""
        if self.buffer is not None:
            obj = self.buffer
            self.buffer = []
            return obj
        return []

    def get_ip(self):
        """возвращает свой IP-адрес."""
        return self.ip


class Data:
    def __init__(self, data, ip_pur):
        self.data = data
        self.ip_pur = ip_pur


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[
    0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to,
                                             'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
