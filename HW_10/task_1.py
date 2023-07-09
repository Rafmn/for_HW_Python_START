'''
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
'''

import math


class Circle:
    '''Окружность'''
    def __init__(self, radius):
        self.radius = radius

    def circle_len(self):
        '''Длина окружности'''
        return math.pi * 2 * self.radius

    def circle_area(self):
        '''Площадь окружности'''
        return math.pi * self.radius ** 2

a = Circle(5)
print(a.circle_len())
print(a.circle_area())
print(Circle.circle_area(a))
