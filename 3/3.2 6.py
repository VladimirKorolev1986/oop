class RenderList:
    def __init__(self, type_list):
        if type_list not in ['ul', 'ol']:
            self.type_list = 'ul'
        else:
            self.type_list = type_list

    def __call__(self, lst, *args, **kwargs):
        s = ''
        for i in lst:
            s += f'<li>{i}</li>\n'
        return f'<{self.type_list}>{s}</{self.type_list}>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)