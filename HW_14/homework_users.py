import json

class MyExteption(Exception):
    pass

class ExteptionLevel(MyExteption):
    def __init__(self, level, name, *args: object) -> None:
        super().__init__(*args)
        self.level = level
        self.name = name

    def __str__(self) -> str:
        return f'Level {self.level} incorrect for {self.name}!'

class ExteptionAccess(MyExteption):
    def __init__(self, user_id, *args: object) -> None:
        super().__init__(*args)
        self.user_id = user_id

    def __str__(self) -> str:
        return f'Access for {self.user_id} denied!'


class User:
    def __init__(self, user_id, name, level=None):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Пользователь.\t Идентификационный номер: {self.user_id},\t имя: {self.name},\t \
            уровень доступа: {self.level}\n'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name


def add_user_to_file(filename): # Ручное добавление пользователя
    try:
        with open(filename, "r", encoding="utf-8") as f:
            my_dict = json.load(f)
    except Exception:
        my_dict = {str(level): {} for level in range(1, 8)}
    print(f'{my_dict = }')
    while True:
        name, user_id, level, * \
            _ = input(
                "Введите имя, личный идентификатор и уровень доступа через пробел: ").split()
        # если идентификатора нет в ключах словаря, то добавляем пару {идентификатор : имя} в
        # словарь
        try:
            if user_id not in my_dict[level].keys():
                my_dict[level].update({user_id: name})
                break
            else:
                print('Идентификатор не уникален')
        except KeyError as err:
            print(f'Ошибка ввода уровня {err}')
    print(f'{my_dict = }')
    with open(filename, "w", encoding="utf-8") as f:
        # записываем словарь в json-файл с отступом=1
        json.dump(my_dict, f, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    FILE_NAME = 'users.json'
    user_1 = User('2', 'Petr', 4)
    user_2 = User('3', 'Katya', 7)
    print(user_1 == user_2)
    add_user_to_file(FILE_NAME)

class Project:
    def __init__(self, users):
        self.users = users
        self.admin = None

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as fnm:
                users_dct = json.load(fnm)
        except Exception as err:
            print(f'При открытии файла {filename} возникла ошибка {err}')
        else:
            # print(f'{users_dct = }')
            users = []
            for level, user in users_dct.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))
            return Project(users)
    
    def __str__(self) -> str:
        return str(self.users)
    
    def login(self, user_id, name):
        new_user = User(user_id, name)
        if new_user not in self.users:
            raise ExteptionAccess(user_id)
        for user in self.users:
            if new_user == user:
                self.admin = user

    def add_user(self, user_id, name, level):
        if int(self.admin.level) <= int(level):
            raise ExteptionLevel(level, name)
        self.users.append(User(user_id, name, level))

if __name__ == "__main__":
    FILE_NAME = 'users.json'
    project = Project.load(FILE_NAME)
    print(*project.users)
    project.login('34', 'Maraska')
    print(project.admin)
    project.add_user('3', 'Nikita', '7')
