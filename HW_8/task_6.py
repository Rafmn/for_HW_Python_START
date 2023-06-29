'''
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
Для тестированию возьмите pickle версию файла из предыдущей задачи. 
Функция должна извлекать ключи словаря 
для заголовков столбца из переданного файла.
'''

import pickle
import csv


def pick_to_csv(pick_file, csv_file):
    '''Перезапись из pickle в csv'''
    with (open(pick_file, 'rb') as pick_f,
          open(csv_file, 'w', encoding='utf-8') as csv_f):
        my_dict = pickle.load(pick_f)
        keys_my_dict = [k for k in my_dict[0].keys()]
        csv_write = csv.DictWriter(csv_f,
                                   fieldnames=keys_my_dict, dialect='excel-tab')
        # запись заголовка
        csv_write.writeheader()
        # матрица
        csv_write.writerows(my_dict)


if __name__ == '__main__':
    pick_to_csv('HW_8/user.pickle', 'HW_8/user.csv')
