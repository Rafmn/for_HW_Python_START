def set_url(url):
    if '/' in url:
        slash = '/'
    else:
        slash = '\\'
    list_url = url.split(slash)
    way = '/'.join(list_url[:-1]) + '/'
    file = list_url[-1].split('.')
    file_name = file[0]
    file_format = '.' + file[1]
    return (way, file_name, file_format)

print(set_url(input('any_url: ')))
