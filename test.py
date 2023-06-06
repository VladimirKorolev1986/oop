class VK:
    def __init__(self):
        self.name = 'VK'


class Youtube:
    def __init__(self):
        self.name = 'Youtube'


class APP:
    def __init__(self):
        self.lst = []

    def verify(self, obj):
        if all(map(lambda x: type(x) == obj, self.lst)):
            self.lst.append(obj)
