'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def factorial(number):
    '''
    Факториал числа n.
    '''
    number = 1
    for i in range(1, number + 1):
        number *= i
        yield number


for j, num in enumerate(factorial(10), start=1):
    print(f'{j}! = {num}')
