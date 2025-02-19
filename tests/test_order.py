import allure
import pytest
from data import Data
from api_methods import ApiMethods

class TestOrder:
    @allure.title('Проверка того, что в заказе можно указать цвета BLACK или GREY, или оба цвета,'
                  'или не указывать цвет вообще')
    @allure.description('Создаётся заказ, по окончании проверяется статус-код успешного заказа')
    @pytest.mark.parametrize(
        'color',
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_orders_color_is_black_or_grey(self, color):
        Data.DATA_FOR_ORDERS["color"] = color
        response = ApiMethods.create_order(Data.DATA_FOR_ORDERS)
        assert response.status_code == 201 and 'track' in response.text
