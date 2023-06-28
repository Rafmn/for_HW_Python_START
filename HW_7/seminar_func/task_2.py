'''
Задача 2. Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.
'''

from random import choice, randint

COUNT_NAMES = 5
VOVELS = 'eyuioa'
CONSONANT = 'qwrtpsdfghjklzxcvbnm'
MIN_LENGTH = 4
MAX_LENGTH = 7


def task_2(count_names, filename):
    '''
    Генерация псевродимен
    '''
    lenn = randint(MIN_LENGTH, MAX_LENGTH)
    names = []
    for _ in range(count_names):
        name = []
        letter = choice(VOVELS)
        name.append(letter)
        for _ in range(lenn-1):
            name.append(choice(CONSONANT))
        name = ''.join(name).capitalize()
        names.append(name)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(names))


if __name__ == '__main__':
    FILENAME = 'HW_7/names.txt'
    task_2(COUNT_NAMES, FILENAME)
    