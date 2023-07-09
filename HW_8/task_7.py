'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку.
'''

import csv
import pickle


def read_csv(csv_file):
    '''Распечатывание csv как pickle'''
    with open(csv_file, 'r', encoding='utf-8', newline='') as csv_f:
        read_csv_file = csv.reader(csv_f, dialect='excel-tab')
        # Преобразование в словарь
        list_csv = []
        for i in read_csv_file:
            list_csv.append(i)
        dict_list_csv = [dict(zip(list_csv[0], list_csv[i]))
                         for i in range(1, len(list_csv))]
        print(dict_list_csv)

        res = pickle.dumps(dict_list_csv, protocol=pickle.DEFAULT_PROTOCOL)
        print(res)


if __name__ == '__main__':
    read_csv('HW_8/user.csv')
