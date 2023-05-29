class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(self.__next, StackObj) or self.__next is None:
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка;"""
        if not self.top:
            self.top = obj
        else:


    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка;"""
        pass

    def get_data(self):
        """получение списка из объектов односвязного списка
        (список из строк локального атрибута __data каждого объекта в порядке их добавления,
        или пустой список, если объектов нет)"""
        pass



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']