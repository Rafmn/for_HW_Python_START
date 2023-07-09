'''
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного 
ФИО и т.п. на ваш выбор.
Cвойство возраст должно быть недоступно для прямого обращения, но возможность получить текущий 
возраст должна присутствовать.
'''

class Human:
    '''Личность'''
    def __init__(self, age, surname, name, patronimic):
        self.__age = age
        self.surname = surname
        self.name = name
        self.patronimic = patronimic

    def birthday(self):
        '''День роджения'''
        self.__age += 1

    def get_age(self):
        '''Возраст'''
        return self.__age

    def full_name(self):
        '''Полное имя'''
        return f'{self.surname} {self.name} {self.patronimic}'


if __name__ == '__main__':
    a = Human(19, "Smirniva", "Katya", "Sergeevna")
    a.birthday()
    print(a.full_name(), a.get_age())
