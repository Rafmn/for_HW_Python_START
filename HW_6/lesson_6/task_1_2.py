__all__ = ["my_func"]

from random import randint
import sys

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
a = 10


def my_func(LOWER_LIMIT, UPPER_LIMIT, a):
    count = 0
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    while count < a:
        dig = int(input(f'Попытка {10 - count} Введите число > '))
        count += 1
        if dig < num:
            print ('Больше')
        elif dig > num:
            print ('Меньше')
        elif dig == num:
            print ('Ура! Вы угадали')
            return True
        if count == 10:
            print(f'Увы... Загаданное число {num}')
            return False


print(my_func(LOWER_LIMIT, UPPER_LIMIT, a))

if __name__ == '__main__':
    _, LOWER_LIMIT, UPPER_LIMIT, a = sys.argv
    my_func(int(LOWER_LIMIT), int(UPPER_LIMIT), int(a)) 