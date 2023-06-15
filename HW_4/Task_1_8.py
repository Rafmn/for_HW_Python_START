# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def rename_l(alist):
    new_list = []
    for i in range(len(alist)):
        n, m = alist[i].split('=')
        if len(n)>1 and n[-1] == 's':
            new_list.append(n + '=' + 'None')
            new_per = n[:-1] + '=' + m
            new_list.append(new_per)
        else:
            new_list.append(alist[i])
    return new_list


list_per = ['as=456', 'word=446', 's="sssg"', 'names=4456', 'cars=345', 'squart=34556']

for i in rename_l(list_per):
    print(i)
