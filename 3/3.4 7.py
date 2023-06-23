class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
            return self
        self.book_list.pop(other)
        return self

    def __isub__(self, other):
        self.__sub__(other)
        return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


lib = Lib()
book = Book('Капитанская дочка', 'Пушкин', 1898)
book1 = Book('Война и мир', 'Толстой', 1900)

lib = lib + book  # добавление новой книги в библиотеку
lib += book

lib = lib - book  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx  # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx
