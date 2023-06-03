# Задача 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
a_try = 10
my_num = int(input("Введите число от 0 до 1000: "))

while num != my_num or a_try >= 0:
    a_try -= 1
    if my_num < num:
        my_num = int(input(f"Загаданное число больше. Осталось попыток: {a_try}. Введите новое число: "))
    elif my_num > num:
        my_num = int(input(f"Загаданное число меньше. Осталось попыток: {a_try}. Введите новое число: "))

print("Было загадано число", num)
