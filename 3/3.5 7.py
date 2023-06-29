filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]


class FileAcceptor:
    def __init__(self, *args):
        self._ext = args

    def __call__(self, filename):
        lst = []
        if isinstance(filename, list):
            for i in filename:
                lst.append(i.split('.')[::-1][0])
            return set(self._ext) >= set(lst)
        else:
            if filename.split('.')[::-1][0] in self._ext:
                return filename

    def __add__(self, other):
        return FileAcceptor(*set(list(self._ext) + list(other._ext)))


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
print(acceptor12.__dict__)

filenames = list(filter(acceptor, filenames))
