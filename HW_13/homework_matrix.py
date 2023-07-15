'''
Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц

Возьмите 1-3 задачи из тех, что были на прошлых семинарах или 
в домашних заданиях. Напишите к ним классы исключения с выводом 
подробной информации. Поднимайте исключения внутри основного кода. 
'''

class Matrix:
    '''Действия с матрицами'''

    def __init__(self, matrix):
        self.matrix = matrix
        self.check_matx()

    def check_matx(self):
        '''Проверка целостности матрицы'''
        len_m = len(self.matrix[0])
        for i in self.matrix:
            if len(i) != len_m:
                raise MatrixCorrectExteption(self.matrix)
            for j in i:
                if isinstance(j, int) is False and isinstance(j, float) is False:
                    raise MatrixDigitalExteption(j, self.matrix)


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
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixSubAddExteption
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
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise MatrixSubAddExteption
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
        if len(self.matrix) != len(other.matrix[0]):
            raise MatrixMultExteption
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

class MyExteption(Exception):
    def __init__(self, marx, *args: object) -> None:
        super().__init__(*args)
        self.marx = marx

class MatrixMultExteption(MyExteption):
    def __init__(self, marx) -> None:
        super().__init__(marx)

    def __str__(self):
        return 'Умножение матриц невозможно. Ширина одной матрицы должна равняться длине другой'

class MatrixSubAddExteption(MyExteption):
    def __init__(self, marx) -> None:
        super().__init__(marx)

    def __str__(self):
        return 'Размер матриц для сложения или вычитания должен быть одинаков'

class MatrixCorrectExteption(MyExteption):
    def __init__(self, marx) -> None:
        super().__init__(marx)

    def __str__(self) -> str:
        return f'Матрица {self.marx} не полная. Длины всех строк должны быть равны'

class MatrixDigitalExteption(MyExteption):
    def __init__(self, j, marx) -> None:
        super().__init__(marx)
        self.j = j

    def __str__(self) -> str:
        return f'Матрица {self.marx} содержит некорректное значение: {type(self.j), self.j}. \
            Матрица должна содержать числа'


a = Matrix([[2, 4, 5], [3, 0.5, 7]])
b = Matrix([[6, 4], ['3', 2], [4, 7]])
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
