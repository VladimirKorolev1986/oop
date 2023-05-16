class Server:
    ip = 1

    def __init__(self):
        self.ip += 1
        Server.ip = self.ip


class Router:
    pass


class Data:
    pass


sv0 = Server()
sv1 = Server()
sv2 = Server()

print(sv0.ip)
print(sv0.ip)
print(sv0.ip)
