'''
Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов. 
* При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла. 

Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
'''

import os


DIR = '/home/marat/GeekBrains/PythonDeeping/for_HW_Python_START-1/HW_7/Files/'
# DIR = r"C:\Users\User\Documents\DeepingPython\Seminar_7\HW_7\Files\\"
# DIR = os.getcwd()


def rename(old_extension, new_extension, new_file_name, dir_):
    '''Переименование файлов'''
    files = [file for file in os.listdir(dir_) if os.path.isfile(os.path.join(dir_, file))]
    for old_file in enumerate(files, 1):
        if old_file[1].split('.')[1] == old_extension:
            new_file = '_'.join((old_file[1].split('.')[0], new_file_name, str(old_file[0]))) + '.' + new_extension
            os.replace(os.path.join(dir_, old_file[1]), os.path.join(dir_, new_file))


NEW_FILE_NAME = 'NewName'

if __name__ == '__main__':
    rename('txt', 'doc', NEW_FILE_NAME, DIR)
