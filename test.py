lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
s=''
for i in lst:
    s += f'<li>{i}</li>\n'

print(s)