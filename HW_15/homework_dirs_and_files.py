'''
Получает на вход директорию и рекурсивно обходит её и все 
вложенные директории.
'''

from collections import namedtuple
import logging
import os

DIR = r'/home/marat/GeekBrains/PythonDeeping/for_HW_Python_START-1/HW_15'
FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d}\
      функция "{funcName}()" в {created}  {msg}'
logging.basicConfig(filename='loghomework',
                    filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger()

def files_dir(dir_):
    '''Составление списка папок и файлов'''
    AOject = namedtuple(
    'Object', ['name_object', 'extension_object', 'flag_dir', 'parent_dir'])

    for dir_path, dir_name, file_name in os.walk(dir_):
        # Родительская директория:
        parent_dir = dir_path.rsplit('/', 1)[-1]
        if parent_dir is None:
            parent_dir = dir_.rsplit('/', 1)[-1]
        # Списки файлов и папок:
        for i in file_name:
            file_name = i.split('.')[0]
            try:
                file_extension = i.split('.')[1]
            except IndexError:
                file_extension = 'None'
            a_object = AOject(file_name, file_extension, False, parent_dir)
            logger.info(a_object)
        for j in dir_name:
            b_object = AOject(j, 'None', False, parent_dir)
            logger.info(b_object)


if __name__ == '__main__':
    files_dir(DIR)
