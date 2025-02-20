import allure
from api_methods import ApiMethods

class TestListOfOrders:
    @allure.title('Проверка, что в ответе на запрос списка заказов возвращается список')
    @allure.description('Отправляется запрос на получение списка заказов, проверяется статус-код успеха'
                        'и содержания слова "orders" в ответе (списка заказов)')
    def test_list_of_orders(self):
        response = ApiMethods.get_list_of_orders()
        assert response.status_code == 200 and "orders" in response.text
