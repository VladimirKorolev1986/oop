stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

lst_words = []
lst_lst = []
for w in stich:
    for s in w.split():
        s = s.replace('–', '')
        s = s.replace('?', '')
        s = s.replace('!', '')
        s = s.replace(',', '')
        s = s.replace('.', '')
        s = s.replace(';', '')
        if s:
            lst_words.append(s)
    lst_lst.append(lst_words)
    lst_words = []


class StringText:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        return len(self.s) < len(other.s)

    def __le__(self, other):
        return len(self.s) < len(other.s)

    def __len__(self):
        return len(self.s)


lst_text = [StringText(x) for x in lst_lst]

lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)

lst_text_sorted = list(map(lambda x: ' '.join(x.s), lst_text_sorted))
