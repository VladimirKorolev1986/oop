class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        obj = super().__new__(Point)
        obj.x = self.x
        obj.y = self.y
        return obj

pt = Point(1, 2)
print(f'{id(pt)}  ---x  -  {pt.x},  y =  {pt.y}')
pt_clone = pt.clone()
print(pt_clone.x)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#
# pt = Point(1, 2)
# pt_clone = pt.clone()
