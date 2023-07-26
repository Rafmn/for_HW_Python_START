'''
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
'''

import pytest
from homework_users import Project, User




class TestExample:
    # def test_1(self, generate_data): # Прокидываем фикстуру в тест и она выполнится перед тестом
    #     login = generate_data[0] # Записываем в переменную сгенерированный логин
    #     login_id = generate_data[1] # Записываем в переменную полученный id
    #     access = generate_data[2]  # Записываем в переменную полученный уровень доступа

    def test2(self, project):
        '''Создание проекта'''
        assert isinstance(project, Project), 'Нет такого файла'

    def test4(self, project):
        assert project.login

    def test3(self, project):
        assert project.add_user('723', 'Pavel', 2) in project.users, 'Пользователь не добавлен'


if __name__ == "__main__":
    pytest.main()
