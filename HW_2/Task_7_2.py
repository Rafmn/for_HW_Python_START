# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

num = int(input('Введите число для преобразования в шестнадцатеричную систему: '))
num_hex = num
sixth = ''

while num > 16:
    a = num % 16
    num = num // 16
    match a:
        case 10:
            a = 'A'
        case 11:
            a = 'B'
        case 12:
            a = 'C'
        case 13:
            a = 'D'
        case 14:
            a = 'E'
        case 15:
            a = 'F'
        case _:
            pass
    sixth += str(a)

sixth += str(num)
sixth = sixth[::-1]

print(num_hex, '->', sixth)
print('Проверка', hex(num_hex)[2:].upper())
    
