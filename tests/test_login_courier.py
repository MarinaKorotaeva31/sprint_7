import allure
import requests
from urls import Urls
from data import Data
from api_methods import ApiMethods

class TestLoginCourier:

    @classmethod
    def setup_class(cls):
        data_for_reg = ApiMethods.register_new_courier_and_return_login_password()
        ApiMethods.create_account(data_for_reg[0], data_for_reg[1], data_for_reg[2])
        cls.login_cls = data_for_reg[0]
        cls.password_cls = data_for_reg[1]

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Осуществляется вход в аккаунт, проверяется статус-код запроса')
    def test_authorization_courier(self):
        response = ApiMethods.login_courier(self.login_cls, self.password_cls)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка невозможности входа при вводе неверного логина')
    @allure.description('Осуществляется вход с изменённым логином, проверяется статус-код')
    def test_login_wrong_password(self):
        response = ApiMethods.login_courier(f"{self.login_cls}123", self.password_cls)
        assert response.status_code == 404 and response.json()['message'] == Data.CODE_404

    @allure.title('Проверка невозможности входа при вводе неверного пароля')
    @allure.description('Осуществляется вход с изменённым паролем, проверяется статус-код')
    def test_login_wrong_password(self):
        response = ApiMethods.login_courier(self.login_cls, f"{self.password_cls}123")
        assert response.status_code == 404 and response.json()['message'] == Data.CODE_404

    @allure.title('Проверка невозможности входа без заполнения обязательного поля')
    @allure.description("Осуществляется вход в аккаунт без пароля")
    def test_login_without_required_field(self):
        response = requests.post(url=Urls.login_api, json={"login": self.login_cls})
        assert response.status_code == 400 and response.json()['message'] == Data.CODE_400_login

    @allure.title('Проверка невозможности входа без заполнения обязательного поля')
    @allure.description("Осуществляется вход в аккаунт без логина")
    def test_login_without_required_field(self):
        response = requests.post(url=Urls.login_api, json={"password": self.password_cls})
        assert response.status_code == 400 and response.json()['message'] == Data.CODE_400_login

    @allure.title('Проверка невозможности входа в несуществующий аккаунт')
    @allure.description('Осуществляется вход по несуществующим логину и паролю')
    def test_login_non_existent_courier(self):
        response = ApiMethods.login_courier(Data.LOGIN, Data.PASSWORD)
        assert response.status_code == 404 and response.json()['message'] == Data.CODE_404

    @allure.title('Проверка того, успешный вход возвращает id')
    @allure.description('Осуществляется вход с существующими логином и паролем, проверяет статус-код'
                        'успешного входа и содержания id в тексте ответа')
    def test_success_login_return_id(self):
        response = ApiMethods.login_courier(self.login_cls, self.password_cls)
        assert response.status_code == 200 and 'id' in response.text

    @classmethod
    def teardown_class(cls):
        id_courier = ApiMethods.login_courier(cls.login_cls, cls.password_cls).json()['id']
        ApiMethods.delete_courier(id_courier)
