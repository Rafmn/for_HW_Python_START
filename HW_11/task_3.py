'''
Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. 
При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, 
а не длинну и ширину. При вычитании не допускайте отрицательных значений.

Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади. 
Должны работать все шесть операций сравнения

Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
'''


class Rectangle:
    '''Прямоугольник'''
    def __init__(self, side1, side2=None):
        '''Свойства'''
        if side2 is None:
            self.side1 = self.side2 = side1
        else:
            self.side1 = side1
            self.side2 = side2

    def perimetr(self):
        '''Периметр'''
        return 2 * (self.side1 + self.side2)

    def area(self):
        '''Площадь'''
        return self.side1 * self.side2

    def __add__(self, other):
        '''Сложение'''
        p = self.perimetr() + other.perimetr()
        return Rectangle(p // 2 / 2, p // 2 / 2)

    def __sub__(self, other):
        '''Вычитание'''
        p = self.perimetr() - other.perimetr()
        return Rectangle(abs(p // 2 / 2), abs(p // 2 / 2))

    def __eq__(self, other):
        '''Проверка равенства 1'''
        return self.area() == other.area()

    def __gt__(self, other):
        '''Проверка равенства 2'''
        return self.area() > other.area()

    def __lt__(self, other):
        '''Проверка равенства 3'''
        return self.area() < other.area()

    def __ge__(self, other):
        '''Проверка равенства 4'''
        return self.area() >= other.area()

    def __le__(self, other):
        '''Проверка равенства 5'''
        return self.area() <= other.area()

    def __str__(self) -> str:
        return f'Экземпляр класса Rectangle со сторонами "{self.side1}" и "{self.side2}"'

    def __repr__(self) -> str:
        return f'Rectangle ({self.side1}, {self.side2})'


res_1 = Rectangle(5, 5)
res_2 = Rectangle(7, 7)
print(f'{res_1.perimetr() = }\n{res_2.perimetr() = }')
res_3 = res_1 + res_2
res_4 = res_1 - res_2
print(f'{res_3.perimetr() = }\n{res_4.perimetr() = }')
print(f'{res_3.side1 = }\n{res_3.side2 = }')
print(f'{res_4.side1 = }\n{res_4.side2 = }')
print(res_1 == res_2)
print(res_3 >= res_4)
print(res_1)
print(res_3)
