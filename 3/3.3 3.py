class Model:
    def __init__(self):
        self.dct = None

    def query(self, **kwargs):
        self.dct = kwargs

    def __str__(self):
        if self.dct is not None:
            s = ''
            for k, v in self.dct.items():
                s += f'{k}={v}, '
            s = s.rstrip(', ')
            return f'Model: {s}'
        return 'Model'


model = Model()
# model.query(id=1, fio='Sergey', old=33)
print(model)
