# Задание 1 - 9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

# for i in range(2, 10):
#     for j in range(2, 11):
#         print(i, "X", j, "=", i*j)
#     print()

a = []
for i in range(2, 11):
    a1 = []
    for j in range(1, 5):
        a1.append(str(j+1) + " X " + str(i) + " = " + str(i*(j+1)) + "  ")
    a.append(a1)
print(a)

print()

for i in range(2, 11):
    for j in range(5, 10):
        print(j+1, "X", i, "=", i*(j+1), end="    ")
    print()