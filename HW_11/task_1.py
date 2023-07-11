'''
Создайте класс МояСтрока где будут доступны все возможности str и дополнительно 
хранится имя автора строки и время создания (time.time)

Добавьте к задачам 1 и 2 строки документации для классов.

Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
'''

import time

# class MyString(str):
#     def __init__(self, name) -> None:
#         self.name = name
#         self.time = time.time()

class MyString(str):
    '''Строка'''
    def __new__(cls, value, name):
        '''Added the name and the time parameters'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance

    def __str__(self) -> str:
        return f'Экземпляр класса MyString с именем "{self.name}" и строкоей "{self.time}"'

    def __repr__(self) -> str:
        return f'MyString ({self.name}, {self.time})'


string_1 = MyString('nwe', 'str_1')
print(string_1)
print(string_1.upper())
print(string_1.capitalize())
print(string_1.time)
print(string_1.name)
print(string_1)
print(repr(string_1))
