class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if not self.top:
            self.top = obj
        else:


    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self.__data = self.__next = None
        self.data = data
        self.next = None

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
        self.__next = obj
