'''
Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали. 
Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов 
методов экземпляра.

Seminar_8 task_2:
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень 
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

# def func(file_json):
#     '''Запись в файл json'''
#     if os.path.isfile(file_json):
#         with open(file_json, 'r', encoding='utf-8') as f:
#             dct = json.load(f)
#     else:
#         dct = {str(i): {} for i in range(1, 8)}

#     while True:
#         data = input('Введите через пробел имя, id, уровень доступа: ')
#         if not data:
#             break
#         user_input, a_id, access = data.split()
#         if a_id not in dct[access]:
#             dct.setdefault(access, {a_id: user_input})[a_id] = user_input

#     with open(file_json, 'w', encoding='utf-8') as f:
#         json.dump(dct, f, ensure_ascii=False)

import json
import os


class SaveJson:
    '''Запись данных в json файл'''
    _file_json = 'users.json'

    def __init__(self) -> None:
        self._dct = self._check_file()

    def _check_file(self):
        '''Проверка наличия файла'''
        if os.path.isfile(self._file_json):
            with open(self._file_json, 'r', encoding='utf-8') as f:
                dct = json.load(f)
        else:
            dct = {str(i): {} for i in range(1, 8)}
        return dct

    def input_info(self):
        '''Ввод данных'''
        while True:
            data = input('Введите через пробел имя, id, уровень доступа: ')
            if not data:
                return f'Сформирован файл {self._file_json} в текущем каталоге'
            user_input, a_id, access = data.split()
            if a_id not in self._dct[access]:
                self._dct.setdefault(access, {a_id: user_input})[
                    a_id] = user_input
                self._write_into_json()

    def _write_into_json(self):
        '''Запись в файл json'''
        with open(self._file_json, 'w', encoding='utf-8') as f:
            json.dump(self._dct, f, ensure_ascii=False)


a_file = SaveJson()
print(a_file.input_info())
