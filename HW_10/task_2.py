'''
Задание №2
📌 Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие периметр
и площадь.
📌 Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''


class Rectangle:
    '''Прямоугольник'''
    def __init__(self, side1, side2=None):
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


a = Rectangle(5)
b = Rectangle(5, 10)
print(a.perimetr(), a.area())
print(b.perimetr(), b.area())
