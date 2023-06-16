# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def f_dict(**args):
    new_dict = {}
    for v, k in args.items():
        # try:
        #     new_dict[k] = v
        # except TypeError:
        #     new_dict[str(k)] = v
        if k.__hash__:
            new_dict[k] = v
        else:
            new_dict[str(k)] = v
        
    return new_dict


print(f_dict(a_list=[2, 56, 67], mad=56, car='Hello'))
