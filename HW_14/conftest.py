import pytest
from homework_users import Project, User, add_user_to_file


# @pytest.fixture
# def generate_user():
#     login = "autotest"  # Генерирует логин
#     a_id = '512'  # Назначаем идентификатор
#     a_access = 4  # Назначение уровня доступа
#     # Возвращает логин, идентификатор и уровень доступа
#     return {"login": login, "id": a_id, 'access': a_access}

@pytest.fixture  #
def project():
    filename = "users.json"
    return Project.load(filename)

@pytest.fixture
def admin(project):
    project.login("453", "Marat")
    return project

@pytest.fixture
def add_user(project):
    project.login("433", "Marat", 1)
    return project

# @pytest.fixture
# def user(project):
#     login = "Autotest"  # Генерируем логин
#     a_id = '512'  # Назначаем идентификатор
#     a_access = 4  # Назначение уровня доступа
#     a_user1 = User(login, a_id, a_access)
#     return project, a_user1
