'''
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. 
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

import argparse
from homework_dirs_and_files import files_dir

parser = argparse.ArgumentParser(description='About a directory')
parser.add_argument('pdir', type=str, help='Path to directory')
apath = parser.parse_args()

files_dir(apath.pdir)
