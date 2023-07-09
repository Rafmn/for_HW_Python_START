'''
Задание №5
📌 Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

Задание №6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс
Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.

Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''


class Animals:
    '''Животные'''
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        '''Название животного'''
        return self.name


class Fish(Animals):
    '''Рыбы'''
    def __init__(self, fresh_water, deep, fin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fin = fin
        self.fresh_water = fresh_water
        self.deep = deep

    def specific(self):
        '''Особенность плавника'''
        fin_length = self.fin * 0.5
        return fin_length

    def chek_water(self):
        '''Водоплавающее'''
        if self.fresh_water:
            return True
        return False

    def chek_deep(self):
        '''Глубоководность'''
        if self.deep < 3:
            return f'Мелководное до {self.deep} метров'
        elif 3 <= self.deep < 20:
            return f'Среднеглубинное до {self.deep} метров'
        else:
            return 'Глубоководное'

    def info_animal(self):
        '''Общая информация'''
        print(
            f'''Наименование: {self.name}, Наличие хвоста: {self.tail}, Особенность плавника: {self.specific()} 
                Водоплавающее: {self.chek_water()}, Глубоководность: {self.chek_deep()}''')


class Cats(Animals):
    '''Кошачьи'''

    def __init__(self, name, tail, area, size, home=None):
        super().__init__(name, tail)
        self.area = area
        self.size = size
        self.home = home

    def check_home(self):
        '''Прирученность'''
        if self.home:
            return 'Домашняя'
        else:
            return 'Дикая'

    def chek_size(self):
        '''Размерность'''
        if self.size < 0.5:
            return 'Кошка до 0,5 метров'
        else:
            return 'Львы или тигры'

    def info_animal(self):
        '''Общая информация'''
        print(
            f'''Наименование: {self.name}, Наличие хвоста: {self.tail}, 
                Прирученность: {self.check_home()}, Среда обитания: {self.area}, 
                    Размерность: {self.chek_size()}''')


class Dogs(Animals):
    '''Собаки'''

    def __init__(self, name, tail, home):
        super().__init__(name, tail)
        self.home = home

    def check_home(self):
        '''Прирученность'''
        if self.home:
            return 'Домашняя'
        return 'Дикая'

    def info_animal(self):
        '''Общая информация'''
        print(
            f'Наименование: {self.name}, Наличие хвоста: {self.tail}, Прирученность: {self.check_home()}')

class Fabric():
    '''Фабрика классов'''
    def __init__(self, a_type_animal, *param, **kwargs) -> None:
        self.a_animal = a_type_animal(*param, **kwargs)


shark = Fish('es', 2, 6, 'Shark', 'yep')
print(f'Водоплавающее: {shark.chek_water()}',
      shark.chek_deep(), f'Хвост: {shark.tail}', sep=', ')
murmur = Cats('Pers', 'yes', 'Asia', 0.4, 'Yes')
pudel = Dogs('Pudel', 'Yes', 1)

pudel.info_animal()
murmur.info_animal()
shark.info_animal()

volf = Fabric(Dogs, 'Volf', 'yes', None)
volf.a_animal.info_animal()

makaka = Fabric(Cats, 'Tiger', 2, 'Europe', 5)
print(makaka.a_animal.check_home())
