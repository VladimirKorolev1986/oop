class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        if b > len(self.lst_data) - 1:
            b = len(self.lst_data) - 1
        lst = []
        for i in range(a, b + 1):
            lst.append(dict(zip(self.FIELDS, self.lst_data[i].split())))
        return lst

    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split())))

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

db = DataBase()
db.lst_data = lst_in

print(db.select(1, 5))
