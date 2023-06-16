# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def rename_l(**alist):
    second_dict = {}
    for k, v in alist.items():
        if len(k)>1 and k[-1] == 's':
             new_k = k[:-1]
             second_dict[new_k] = v
             alist[k] = None
    alist.update(second_dict)

    return alist


print(rename_l(ask=456, word=446, s="sssg", names=4456, cars=345, squart=34556))
