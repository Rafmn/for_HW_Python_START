'''
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел 
из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
'''

import csv
import json
from random import randint


def decor_csv(qard_func):
    '''Декоратор генерации csv файла'''
    list_json = []
    def random_func():
        random_abc_csv()
        list_csv = read_csv("random_abc.csv")
        for i in list_csv:
            a, b, c = map(int, i[0].split(' '))
            answer = qard_func(a, b, c)
            list_json.append((a, b, c, answer))
        return list_json
    return random_func

def decor_json(json_):
    '''Декоратор создания файла json'''
    def create_json(list_json):
        json_(list_json)
    return create_json


@decor_csv
def qard_equat(a=1, b=1, c=1):
    '''Решение квадратного уравнения'''
    # Дискриминант:
    d = b**2 - 4 * a * c

    if d > 0:
        x_1 = (-b + d**0.5) / 2 * a
        x_2 = (-b - d**0.5) / 2 * a
        return x_1, x_2
    elif d == 0:
        x = - b / (2 * a)
        return x
    else:
        return 'Нет корней'

def random_abc_csv():
    '''Генерация csv файла с тремя случайными числами в каждой строке'''
    nums_lines = randint(100,1001)
    list_nums = []
    for _ in range(nums_lines):
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 10)
        list_nums.append([a, b, c])
    with open('random_abc.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(list_nums)

def read_csv(file):
    '''Чтение файла csv'''
    with open(file, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return list(reader)

@decor_json
def save_json(a_list):
    '''Запись в файл json'''
    with open('answ_qard.json', 'w', encoding='utf-8') as f:
        json.dump(a_list, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    save_json(qard_equat())
