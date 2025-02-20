import pytest
from api_methods import ApiMethods

@pytest.fixture
def create_login_and_delete_courier():
    response = ApiMethods.register_new_courier_and_return_login_password()
    yield response
    login = ApiMethods.login_courier(response[0], response[1])
    id_courier = login.json()['id']
    ApiMethods.delete_courier(id_courier)
