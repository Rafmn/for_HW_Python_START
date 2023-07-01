'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все 
вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте 
родительскую директорию. 
Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, 
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''

import os
import json
import csv
import pickle

# DIR = r'C:\Users\User\Documents\DeepingPython'
DIR = r'/home/marat/GeekBrains/PythonDeeping/for_HW_Python_START-1'

def files_dir(dir_):
    '''Составление списка папок и файлов'''
    merge_list = []
    for dir_path, dir_name, file_name in os.walk(dir_):
        # Родительская директория:
        parent_dir = dir_path.rsplit('/', 1)[-1]
        # Списки размеров файлов и папок:
        size_file = [os.stat(os.path.join(dir_path, file)).st_size for file in file_name]
        if dir_name:
            size_dir = [size_of_dir(os.path.join(dir_path, dir_)) for dir_ in dir_name]
        # Сшивка размеров с названиями:
        file_name_info = dict(zip(file_name, size_file))
        dir_name_info = dict(zip(dir_name, size_dir))
        # Добавление родительской директории и типа объекта:
        for k, i in file_name_info.items():
            file_name_info[k] = [i, parent_dir, 'file']
        for k, i in dir_name_info.items():
            dir_name_info[k] = [i, parent_dir, 'folder']
        # Объединение словарей в один:
        merge_dict = {**dir_name_info, **file_name_info}

        list_dicts = change_dict(merge_dict)
        for i in list_dicts:
            merge_list.append(i)

    print(merge_list)

    # Запись в json файл:
    with open('files_and_dirs.json', 'w', encoding='utf-8') as f:
        json.dump(merge_list, f)

    # Запись в csv файл:
    keys_my_dict = [k for k in merge_list[0].keys()]
    with open('files_and_dirs.csv', 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, keys_my_dict)
        writer.writeheader()
        writer.writerows(merge_list)

    # Запись в pickle файл:
    with open('files_and_dirs.pickle', 'wb') as f:
        pickle.dump(merge_list, f)
    # res = pickle.dumps(list_dicts, protocol=pickle.DEFAULT_PROTOCOL)
    # print(res)


def sum_of_files(a_folder, file_name):
    '''Сумма файлов в папке'''
    sum_file = sum([os.stat(os.path.join(a_folder, file)).st_size for file in file_name])
    return sum_file


def size_of_dir(a_path, size_folder = 0):
    '''Размер директории со всеми файлами и папками'''
    for dir_path, _, file_name in os.walk(a_path):
        if file_name:
            sum_f = sum_of_files(dir_path, file_name)
            size_folder += sum_f
    return size_folder


def change_dict(a_dict):
    '''Переделка словарей в другой формат записи:'''    
    list_dicts = []
    my_dict = {'Object': [], 'Size_bite': [], 'Parent_dir': [], 'Type': []}
    for k, i in a_dict.items():
        my_dict['Object'] = k
        my_dict['Size_bite'] = i[0]
        my_dict['Parent_dir'] = i[1]
        my_dict['Type'] = i[2]
        list_dicts.append(my_dict.copy())
    return list_dicts


if __name__ == '__main__':
    files_dir(DIR)
