# Задание 1 - 8
# 📌 Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.

n = int(input("Сколько рядов у елки?: "))

stars = 1

for i in range(0, n):
    space = n-i-1
    print(" " * space, "*" * stars, sep='')
    stars += 2
