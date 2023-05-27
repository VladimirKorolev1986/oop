class Clock:
    def __init__(self):
        self.__time = 0

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        if 0 <= tm < 100_000 and isinstance(tm, int):
            return True
        return False


clock = Clock()
clock.set_time(4530)
