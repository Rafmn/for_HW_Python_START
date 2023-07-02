'''
Создайте функцию-замыкание, которая принимает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за 
указанное число попыток.
'''

from random import randint

def make(high, num_of_attempts):
    def game():
        number = randint(1, high)
        attempt = 0
        print(
            f'Программа загадывает число от {1} до {high}. Необходимо угадать число за {num_of_attempts} попыток.')
        while attempt < num_of_attempts:
            attempt += 1
            user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
            if user_number < number:
                print('Меньше')
            elif user_number > number:
                print('Больше')
            else:
                print(f'Вы отгадали с {attempt} попытки!')
                return True
        else:
            print(f'Вы использовали все {attempt} попыток и не отгадали число.\ Было загадано число {number}. Вы проиграли.')
            return False
    return game


if __name__ == '__main__':
    high = 10
    num_of_attempts = 5
    res = make(high, num_of_attempts)
    res()
