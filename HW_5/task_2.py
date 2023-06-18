'''Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.'''

def set_url(url):
    '''
    Принимает адрес и возвращает кортеж.
    '''
    if '/' in url:
        slash = '/'
    else:
        slash = '\\'
    # list_url = url.split(slash)
    # way = '/'.join(list_url[:-1]) + '/'
    list_url = url.rsplit(slash, 1)
    way = list_url[0]
    file = list_url[-1].split('.')
    file_name = file[0]
    file_format = file[1]
    return (way, file_name, file_format)

print(set_url(input('any_url: ')))
