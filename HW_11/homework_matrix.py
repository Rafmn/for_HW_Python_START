'''
Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц
'''

class Matrix:
    '''Действия с матрицами'''

    def __init__(self, matrix):
        self.matrix = matrix
        # return matrix

    def get_matrix(self):
        '''Вывод матрицы'''
        for i in self.matrix:
            print(*i)

    def __str__(self):
        return f'Экземпляр класса Matrix с матрицей "{self.matrix}"'

    def __repr__(self) -> str:
        return f'Matrix ({self.matrix})'

    def __add__(self, other):
        '''Сложение матриц'''
        add_matrix = []
        for i, _ in enumerate(self.matrix):
            a_string = []
            for j in range(len(self.matrix[0])):
                sum_m = self.matrix[i][j] + other.matrix[i][j]
                a_string.append(sum_m)
            add_matrix.append(a_string)
        return Matrix(add_matrix)

    def __sub__(self, other):
        '''Вычитание матриц'''
        sub_matrix = []
        for i, _ in enumerate(self.matrix):
            a_string = []
            for j, _ in enumerate(self.matrix[0]):
                sum_m = self.matrix[i][j] - other.matrix[i][j]
                a_string.append(sum_m)
            sub_matrix.append(a_string)
        return Matrix(sub_matrix)

    def __mul__(self, other):
        '''Умножение матриц'''
        mult_matrix = []
        for i, _ in enumerate(self.matrix):
            a_string = []
            for j, _ in enumerate(self.matrix[0]):
                mult_m = self.matrix[i][j] * other.matrix[j][i]
                a_string.append(mult_m)
            mult_matrix.append(a_string)
        return Matrix(mult_matrix)

    def __eq__(self, __value: object) -> bool:
        '''Сравнение матриц'''
        for i, _ in enumerate(self.matrix):
            for j, _ in enumerate(self.matrix[0]):
                bl = self.matrix[i][j] == __value.matrix[i][j]
                if bl is False:
                    return bl
        return bl

# def __new__():
#     # matr = super().__new__(cls)
#     n = int(input('Количество строк в матрице: '))
#     matr = []
#     for i in range(n):
#         l = list(map(int, input(f'Введите числа через пробел в строке {i+1}: ').split()))
#         matr.append(l)
#     return matr

# a = Matrix(__new__())
# b = Matrix(__new__())

a = Matrix([[2, 4, 5], [3, 5, 7]])
b = Matrix([[6, 4], [3, 2], [4, 7]])
b1 = Matrix([[2, 4, 2], [3, 1, 7]])
b2 = Matrix([[2, 4, 2], [3, 1, 7]])

print(a)
print(repr(a))
print(b)
c = a + b1
print(c)
d = a - b1
print(d)
e = a * b
g = b * a
print(e)
print(g)
print(a == b1)
print(b2 == b1)
