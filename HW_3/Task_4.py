# Создайте словарь со списком вещей для похода в качестве 
# ключа и их массой в качестве значения. Определите какие 
# вещи влезут в рюкзак передав его максимальную 
# грузоподъёмность. Достаточно вернуть один допустимый вариант.


things = dict(book=50, watch=10, matches=2, cup=5, spoon=5, plate=10, fork=4, \
    kompas=6, potatoes=50, bread=25, tea=4, knife=6, T_shirt=5, pen=1, \
    notebook=5, snickers=40)

bag = int(input('Введите максимальную грузоподъемность рюкзака: '))

things_in = []
mass = 0

for key, value in things.items():
    if value + mass <= bag:
        mass += value
        things_in.append(key)

print(f'В рюкзак влезут {len(things_in)} вещей: ', end='')
print(*things_in, sep=', ')