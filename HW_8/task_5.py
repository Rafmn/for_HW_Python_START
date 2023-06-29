'''
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое 
в виде одноименных pickle файлов.
'''

import json
import pickle
import os


def func(dir_):
    '''Поиск и замена файлов .json'''
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for json_file in json_files:
        with (open(os.path.join(dir_, json_file), 'r', encoding='utf-8') as f,
              open(os.path.join(dir_, json_file.strip('.json') + '.pickle'), 'wb') as f_p):
            pickle.dump(json.load(f), f_p)


if __name__ == '__main__':
    func(os.path.join(os.getcwd(), 'HW_8'))
    with open('HW_8/user.pickle', 'rb') as f_pi:
        print(pickle.load(f_pi))
