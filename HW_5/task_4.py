'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def fibon(number):
    '''
    Фибоначи числа n.
    '''
    numb = 1
    last_num = 0
    for i in range(number):
        numb += last_num
        last_num, numb = numb, last_num
        yield numb


for j, num in enumerate(fibon(10), start=1):
    print(f'{j} = {num}')
