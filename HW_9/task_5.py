'''Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
декораторами для сохранения параметров,
декоратором контроля значений и
декоратором для многократного запуска.
Выберите верный порядок декораторов.'''


from task_4 import param as repeat
from task_2 import deco as control
from task_3 import deco as save_json


@repeat(2)
@save_json
@control
def game(number, num_of_attempts):
    attempt = 0
    print(
        f'Программа загадывает число от {1} до {number}. Необходимо угадать число за \
            {num_of_attempts} попыток.')
    while attempt < num_of_attempts:
        attempt += 1
        user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
        if user_number < number:
            print('Больше')
        elif user_number > number:
            print('Меньше')
        else:
            print(f'Вы отгадали с {attempt} попытки!')
            return True
    else:
        print(f'Вы использовали все {attempt} попыток и не отгадали число.\ Было загадано число \
              {number}. Вы проиграли.')
        return False


if __name__ == '__main__':
    game(1000, 2)
