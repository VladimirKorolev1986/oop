class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        x = self.func()
        return [int(x) for x in x.split()]

input_dg = InputDigits(input)
res = input_dg()

