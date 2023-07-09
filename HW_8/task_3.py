'''
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''

import csv
import json


def json_csv(jsonfile):
    '''Перезапись в csv'''
    csvfile = 'HW_8/person.csv'
    with(open(jsonfile, "r", encoding="utf-8") as json_f,
    open(csvfile, "w", newline='', encoding="utf-8") as csv_f):
        json_dict = json.load(json_f)
        print(json_dict)
        rows = []
        for level, in_dict in json_dict.items():
            for a_id, name in in_dict.items():
                rows.append({'id': a_id, 'level': int(level), 'name': name})

        print(rows)

        csv_write = csv.DictWriter(csv_f, fieldnames=['id', 'level', 'name'])
        # запись заголовка
        csv_write.writeheader()
        # матрица
        csv_write.writerows(rows)


if __name__ == '__main__':
    JSONFILE = 'HW_8/users.json'
    json_csv(JSONFILE)
