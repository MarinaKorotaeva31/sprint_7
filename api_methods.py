import allure
import requests
import random
import string
from urls import Urls

class ApiMethods:
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @staticmethod
    @allure.step('Регистрация нового курьера')
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f'{Urls.create_courier}', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    @staticmethod
    @allure.step('Регистрация курьера')
    def create_account(login: str, password: str, first_name: str):
        return requests.post(url=Urls.create_courier, json={"login": login, "password": password, "firstName": first_name})

    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(login: str, password: str):
        return requests.post(url=Urls.login_api, json={"login": login, "password": password})

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(id_courier: str):
        return requests.delete(url=f"{Urls.delete_courier}/{id_courier}")

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(data):
        return requests.post(url=Urls.orders_api, json=data)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_of_orders():
        return requests.get(url=Urls.orders_api)
