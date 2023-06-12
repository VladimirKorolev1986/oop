import math


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == int and args[0] > 1:
            self.coords = list(0 for _ in range(args[0]))
        else:
            self.coords = list(args)

    def set_coords(self, *args):
        i = 0
        for o, t in zip(self.coords, list(args)):
            self.coords[i] = list(args)[i]
            i += 1

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return math.sqrt(sum(list(map(lambda x: x * x, self.coords))))


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
