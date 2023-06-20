'''Задание №7
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.'''

text = input("Введите текст: ").lower()

adict = {}
for letter in text:
    if letter == ' ':
        continue
    elif not letter in adict:
        adict[letter] = 1
    else:
        adict[letter] = adict.get(letter) + 1

print(*adict.items())

dict_count = {}
for letter in text:
    if letter == ' ' or letter in dict_count:
        continue
    else:
        n = text.count(letter)
        dict_count[letter] = n

print(*dict_count.items())
print(adict == dict_count)

# Порядок вывода ключей полностью совпадает
