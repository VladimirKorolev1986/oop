class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    # здесь строчки программы

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            s = func()
            return [self.render(s) for s in s.split()]
        return wrapper


#

class RenderDigit:
    def __call__(self, number, *args, **kwargs):
        try:
            return int(number)
        except:
            return None


render = RenderDigit()
input_dg = InputValues(render)
res = input_dg(input)

print(res())
