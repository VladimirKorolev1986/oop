class SingletonFive:
    __count = 0
    __last_obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__count <= 5:
            cls.__last_obj = super().__new__(cls)
            cls.__count += 1
        return cls.__last_obj

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]

print(objs)
