'''Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.'''

COUNT = 3

def param(count):
    def deco(func):
        res_list= []
        def wrapper(*args):
            for i in range(count):
                res_list.append(func(*args))
            print(res_list)
        return wrapper
    return deco

@param(COUNT)
def my_func(*args):
    return(args)

if __name__ == '__main__':
    my_func('Hello, World!')
