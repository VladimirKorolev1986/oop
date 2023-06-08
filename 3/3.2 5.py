class DigitRetrieve:
    def __call__(self, number, *args, **kwargs):
        if number[0] == '-':
            number = number[1:]
            if number.isdigit():
                return -int(number)
            else:
                return None
        else:
            if number.isdigit():
                return int(number)
            else:
                return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]

print(digits)
