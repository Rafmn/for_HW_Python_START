# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_list(a, b, args):
    # sum_i = 0
    if a > b:
        a, b = b, a
    if a < 0:
        a = 0
    if b > len(args)-1:
        b = len(args)-1
    # for i in range(a, b+1):
    #     sum_i += args[i]
    sum_i = sum(args[a:b+1])
    return sum_i


list_of_nums = list(map(int, input('Введите список чисел через пробел: ').split()))
start_index = int(input('Первый индекс: '))
end_index = int(input('Второй индекс: '))

print(sum_list(start_index, end_index, list_of_nums))
