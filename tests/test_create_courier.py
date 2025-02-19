import allure
import pytest
import requests
from urls import Urls
from data import Data
from api_methods import ApiMethods

class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Создаётся аккаунт, проверяет статус-код и сообщение об успешно создании. Затем логин курьера и удаление аккаунта.')
    def test_create_courier_is_success(self):
        response = ApiMethods.create_account(Data.LOGIN, Data.PASSWORD, Data.FIRST_NAME)
        assert response.status_code == 201 and response.text == Data.CODE_200
        login_courier = ApiMethods.login_courier(Data.LOGIN, Data.PASSWORD)
        id_courier = login_courier.json()['id']
        ApiMethods.delete_courier(id_courier)

    @allure.title('Проверка невозможности создания существующего аккаунта курьера')
    @allure.description('Создаётся аккаунт, после чего повторяется попытка создания курьера с теми же данными. Проверяется статус-код'
                        'и тело ответа. Аккаунт удаляется')
    def test_create_duplicate_is_fall(self, create_login_and_delete_courier):
        response = ApiMethods.create_account(create_login_and_delete_courier[0], create_login_and_delete_courier[1], create_login_and_delete_courier[2])
        assert response.status_code == 409 and response.json()['message'] == Data.CODE_409

    @allure.title('Проверка невозможности создания аккаунта без обязательного параметра')
    @allure.description('Создаётся аккаунт без передачи параметра "логин" или "пароль", проверяется статус-код')
    @pytest.mark.parametrize(
        'payload',
        [
            ({"password": Data.PASSWORD, "firstName": Data.FIRST_NAME}),
            ({"login": Data.LOGIN, "firstName": Data.FIRST_NAME}),
            ({"firstName": Data.FIRST_NAME})
        ]
    )
    def test_create_without_required_field(self, payload):
        response = requests.post(url=Urls.create_courier, json=payload)
        assert response.status_code == 400 and response.json()['message'] == Data.CODE_400

    @allure.title('Проверка невозможности создания аккаунта с пустым логином или паролем')
    @allure.description('Создаётся аккаунт с пустым полем, проверяется статус-код "400" - невозможность создания такого аккаунта')
    @pytest.mark.parametrize(
        'data',
        [
            (['', Data.PASSWORD, Data.FIRST_NAME]),
            ([Data.LOGIN, '', Data.FIRST_NAME]),
        ]
    )
    def test_create_empty_field_is_fall(self, data):
        response = ApiMethods.create_account(data[0], data[1], data[2])
        assert response.status_code == 400 and response.json()['message'] == Data.CODE_400

    @allure.title('Проверка невозможности создания аккаунта курьера с уже существующим логином')
    @allure.description('Создаётся аккаунт, после чего повторяется попытка создания курьера с тем же логином Проверяется статус-код.'
                        'Аккаунт удаляется')
    def test_create_duplicate_login_is_fall(self, create_login_and_delete_courier):
        response = ApiMethods.create_account(create_login_and_delete_courier[0], Data.PASSWORD, Data.FIRST_NAME)
        assert response.status_code == 409 and response.json()['message'] == Data.CODE_409
