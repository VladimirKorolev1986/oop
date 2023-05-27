class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server

    def unlink(self, server):
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None

    def send_data(self):
        for d in self.buffer:
            if d.ip in self.buffer:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()


class Server:
    server_ip = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        if self.buffer is not None:
            obj = self.buffer[:]
            self.buffer.clear()
            return obj
        return []

    def get_ip(self):
        return self.ip

class Data:
    def __init__(self, data, ip_pur):
        self.data = data
        self.ip_pur = ip_pur

