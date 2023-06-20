import time


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        t = self.clock1.get_time() - self.clock2.get_time()
        if t >= 0:
            return time.strftime('%H: %M: %S', time.gmtime(t))
        return '00: 00: 00'

    def __len__(self):
        t = self.clock1.get_time() - self.clock2.get_time()
        if t >= 0:
            return t
        t = 0
        return t


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.__hours = self.__minutes = self.__seconds = None
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if isinstance(hours, int) and hours >= 0:
            self.__hours = hours
        else:
            raise TypeError("Число должно быть целым и не отрицательным")

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if isinstance(minutes, int) and minutes >= 0:
            self.__minutes = minutes
        else:
            raise TypeError("Число должно быть целым и не отрицательным")

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if isinstance(seconds, int) and seconds >= 0:
            self.__seconds = seconds
        else:
            raise TypeError("Число должно быть целым и не отрицательным")

    def get_time(self):
        t = self.hours * 3600 + self.minutes * 60 + self.seconds
        return t


# dt = DeltaClock(clock1, clock2)
# str_dt = str(dt)  # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# len_dt = len(dt)  # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)  # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
