# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

dict = dict(Anton=['ball', 'cup', 'spoon', 'fork'], Igor=['spoon', 'fork', 'cup'], Rinat=['book', 'kompas', 'map', 'cup', 'ball'])

a_list = [] # Списки в одном списке
for value in dict.values():
    list_union = value
    a_list.append(list_union)

set_all = set(a_list[0])
for i in range(1, len(a_list)):
    set_all = set_all.union(a_list[i])
print('Все вещи, которые взяли друзья:', set_all)
print()

for name_1,things_1 in dict.items():
    set_things_1 = set(things_1)
    for name_2, things_2 in dict.items():
        if name_1 == name_2:
            continue
        set_things_2 = set(things_2)
        set_things_1 = set_things_1 - set_things_2
    if len(set_things_1) == 0:
        set_things_1 = 'Таких вещей нет'
    print(f'Уникальные вещи у {name_1}: {set_things_1}')
print() 
   
for name_1,things_1 in dict.items():
    set_things_1 = set(things_1)
    set_things_general = set_all - set_things_1 # Вещи, кторых нет у name_1
    for name_2, things_2 in dict.items():
        if name_1 == name_2:
            continue
        set_things_2 = set(things_2)
        set_things_general = set_things_general & set_things_2
    set_not_thing = set_things_general - set_things_1
    if len(set_not_thing) == 0:
        continue
    print(f'{set_not_thing} есть у всех, кроме {name_1}')
