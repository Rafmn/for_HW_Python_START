'''
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень 
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

import json
import os


def func(file_json):
    '''Запись в файл json'''
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i): {} for i in range(1, 8)}

    while True:
        data = input('Введите через пробел имя, id, уровень доступа: ')
        if not data:
            break
        user_input, a_id, access = data.split()
        if a_id not in dct[access]:
            dct.setdefault(access, {a_id: user_input})[a_id] = user_input

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(dct, f, ensure_ascii=False)


if __name__ == '__main__':
    func('HW_8/users.json')
