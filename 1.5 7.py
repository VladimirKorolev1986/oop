class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = args

    def get_config(self):
        print(f'Материнская плата: {self.name}'
              f'Центральный процессор: {self.cpu.name}, <тактовая частота>'
              f'Слотов памяти: {self.total_mem_slots}'
              f'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>')


cpu = CPU('intel', 2800)
mem = Memory('pioneer', 8)
mb = MotherBoard('asus', cpu, mem)

mb.get_config()
