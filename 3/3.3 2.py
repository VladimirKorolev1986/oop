import sys


class Book:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f"Книга: {self.args[0]}; {self.args[1]}; {self.args[2]}"


lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(*lst_in)
