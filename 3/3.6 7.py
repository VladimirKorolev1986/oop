class DataBase:
    def __init__(self, path):
        self.path = path

    def write(self, record):
        pass

    def read(self, pk):
        pass


class Record:
    pk = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.pk + 1
        Record.pk = self.pk


rec1 = Record(' vova', 'kind', '36')
rec2 = Record('vasya', 'kind', '37')
rec3 = Record('lina', 'kind', '36')

print(rec1.pk)
print(rec2.pk)
print(rec3.pk)
