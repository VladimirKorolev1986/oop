class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a or self.b or self.c is not int:
            return 1


a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)

print(tr.is_triangle())