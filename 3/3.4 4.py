# l1 = [1, 2, 3, 8, 5, 4]
# l1.sort()
# print(l1)


class NewList:
    def __init__(self, *args):
        if args is None:
            self.lst = []
        else:
            self.lst = list(*args)

    def __sub__(self, other: list):
        other = other.lst if isinstance(other, NewList) else other
        return self.__class__([item for item in self.lst if item not in other])

    def __rsub__(self, other: list):
        t = 0
        l_t = []
        other = other.lst if isinstance(other, NewList) else other
        for i in self.lst:

            for j in other:
                if i == j and i is j:
                    l_t.append(t)
            t += 1
        l_t.reverse()
        for i in l_t:
            self.lst.pop(i)

        return NewList(self.lst)


    def get_list(self):
        return self.lst


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
l = lst1 - lst2
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2

print(l)
print(res_2)
print(res_3.lst)
