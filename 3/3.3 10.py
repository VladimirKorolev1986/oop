class PolyLine:
    def __init__(self, *args):
        self.args = list(args)

    def add_coord(self, x, y):
        self.args.append((x, y))

    def remove_coord(self, indx):
        self.args.pop(indx)

    def get_coords(self):
        return self.args


t = PolyLine((1, 2), (2, 4), (4, 6))

print(t.args)
