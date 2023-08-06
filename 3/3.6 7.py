import sys


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        """для добавления новой записи в БД, представленной объектом record;"""
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append

    def read(self, pk):
        """чтение записи из БД (возвращает объект Record)
        по ее уникальному идентификатору pk (уникальное целое положительное число);
        запись ищется в значениях словаря (см. ниже)"""


class Record:
    pk = 1

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.pk
        Record.pk += 1

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return self.fio.lower() == self.fio.lower() and self.old == other.old


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]
