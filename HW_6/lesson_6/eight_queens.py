'''Генерация расстановки ферзей'''

import random


def e_queens(args):
    """Проверка на пересекаемость ферзей"""
    flag = True
    for i in args:
        for j in args:
            a_1, a_2 = map(int, i.split())
            if i != j:
                b_1, b_2 = map(int, j.split())
                if a_1 == b_1 or a_2 == b_2 or a_1 - b_2 == b_1 - b_2:
                    return False

    return True


def random_queens():
    '''Создание случайных координат расстановки ферзей'''
    list_a1 = []
    for _ in range(8):
        a_1 = random.randint(1, 8)
        a_2 = random.randint(1, 8)
        string_1 = str(a_1) + ' ' + str(a_2)
        list_a1.append(string_1)
    return tuple(list_a1)

queens_1 = ('1 3', '2 5', '4 6', '3 8', '2 3', '3 1', '1 7', '4 5')
queens_2 = ('8 5', '6 1', '4 8', '2 4', '7 7', '5 3', '3 6', '1 2')
print(e_queens(queens_1))  # пересекаемые
print(e_queens(queens_2))  # непересекаемые

LIMIT = 4
while LIMIT > 0:   # генерация непересекаемой расстановки
    a_queen = random_queens()
    if e_queens(a_queen):
        LIMIT -= 1
        print(a_queen)
