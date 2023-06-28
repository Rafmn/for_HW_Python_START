'''
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

Дорабатываем функции из предыдущих задач.
* Генерируйте файлы в указанную директорию — отдельный параметр функции.
* Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
* Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

# import os
import random
import string
import os.path


def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_file_size=256,
                                max_file_size=4096, num_files=1):
    '''Генерация файла'''
    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        check_path(DIR)

        file_name = DIR + ''.join(random.choices(
            string.ascii_letters + string.digits, k=name_length)) + '.' + extension
        # генерация имени файла, пока не появится уникальное имя
        while os.path.exists(file_name):
            file_name = DIR + ''.join(random.choices(
                string.ascii_letters + string.digits, k=name_length)) + '.' + extension

        file_size = random.randint(min_file_size, max_file_size)
        # random_bytes = os.urandom(file_size)
        random_bytes = ''.join(random.choices(
            string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open(file_name, 'wb') as file:
            file.write(random_bytes)


def create_dif_files(**kwargs):
    '''Пакет файлов'''
    for ext, num in kwargs.items():
        create_files_with_extension(ext, num_files=num)


def check_path(a_path):
    '''Проверка наличия переданного пути и создание его, при отсутствии'''
    if not os.path.exists(a_path):
        os.mkdir(a_path)


DIR = '/home/marat/GeekBrains/PythonDeeping/for_HW_Python_START-1/HW_7/Files/'

if __name__ == '__main__':
    create_dif_files(txt=2, bin=4, png=8, mp4=3)
    # check_path(DIR)
