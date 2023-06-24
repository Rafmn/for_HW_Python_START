'''Загадки'''

__all__ = ['riddle_box', 'show_result']

def riddle(text="Сорок одежек и все без застежек", solution=['капуста', 'капустка'], attempt=5):
    '''Загадка'''
    count = 1
    print(f'Отгадайте загадку: {text}')
    while count < attempt:
        anm = input('Введите отгадку: ').lower()
        if anm in solution:
            print(f'Вы угадали с {count} попытки')
            return count
        else:
            print('Ошбика')
            count += 1
        if count == attempt:
            print('Вы исчерпали количество попыток')
            return 0


def riddle_box():
    '''Словарь загадок'''
    dic = {"Зимой и летом одним цветом": ["ель", "елка", "елочка"],
           "Не лает, не кусает, в дом не пускает": ['замок', 'вахтер'],
           "Висит груша, нельзя скушать": ['лампа', 'лампочка']}
    for i, j in dic.items():
        riddle_result(i, riddle(i, j))


def riddle_result(text, f_attempt):
    '''_'''
    _result[text] = f_attempt


def show_result():
    output = '\n'.join([f'Вы отгадали задагку "{key}" с {value} попытки' for key, value in _result.items()])
    print(output)
    

_result = {}
