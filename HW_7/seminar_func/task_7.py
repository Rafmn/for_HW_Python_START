'''
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os

DCT = {'Video': ('mvk', 'avi', 'mp4'),
       'Images': ('png', 'jpg', 'jpeg'),
       'Text': ('txt', 'bin')}

def group(dir_):
    '''
    Сортировка
    '''
    files = [file for file in os.listdir(dir_) if os.path.isfile(dir_ + file)]
    for fold, exts in DCT.items():
        if fold not in os.listdir(dir_):
            os.mkdir(dir_ + fold)
        for file in files:
            if file.split('.')[1] in exts:
                os.replace(os.path.join(dir_, file), os.path.join(dir_, fold, file))

# DIR = os.getcwd()
DIR = '/home/marat/GeekBrains/PythonDeeping/for_HW_Python_START-1/HW_7/Files/'


if __name__ == '__main__':
    group(DIR)
