'''
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или 
в домашних заданиях. Напишите к ним классы исключения с выводом 
подробной информации. Поднимайте исключения внутри основного кода. 
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
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
        try:
            float(side1) and float(side2)
        except Exception as ext:
            raise SideExteption(side1, side2) from ext

        if self.side1 <= 0 or self.side2 <= 0:
            raise SideExteption(side1, side2)

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


class MyExteption(Exception):
    pass

class SideExteption(MyExteption):
    def __init__(self, side1, side2) -> None:
        self.side1 = side1
        self.side2 = side2

    def __str__(self) -> str:
        if isinstance(self.side1, str) or isinstance(self.side2, str):
            return 'Значение должно быть числовым'
        else:
            return 'Значение должно быть больше нуля'


a = Rectangle(-5, '3')
print(a.perimetr())
