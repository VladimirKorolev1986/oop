class Translator:
    DCT = {}

    def add(self, eng, rus):
        if self.DCT.get(eng) is None:
            self.DCT[eng] = [rus]
        else:
            self.DCT[eng].append(rus)

    def remove(self, eng):
        del self.DCT[eng]

    def translate(self, eng):
        return self.DCT[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(tr.translate('go'))