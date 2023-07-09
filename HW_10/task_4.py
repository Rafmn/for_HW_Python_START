''''
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания. Используйте импорт класса в новый файл.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь
'''

from random import randint
from task_3 import Human


class Personal(Human):
    '''Сотрудник'''
    MAG = 7

    def __init__(self, id_num, *args, **kwargs):
        self.id_num = self.get_id_num(id_num)
        self.level = self.level_gen()
        super().__init__(*args, **kwargs)

    def level_gen(self):
        '''Уровень доступа'''
        return sum(map(int, list(str(self.id_num)))) % self.MAG

    def get_id_num(self, id_num):
        '''Генерация id'''
        if len(str(id_num)) != 6:
            return randint(100_000, 999_999)
        return id_num

    def get_id(self):
        '''Вывод id'''
        return self.id_num


human1 = Personal(1123, 34, 'Petya', 'Smirnov', 'Fedorov')
print(human1.full_name(), human1.get_id())
