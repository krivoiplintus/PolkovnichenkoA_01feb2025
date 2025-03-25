import allure
from page.company_api import CompanyApi
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider


base_url = ConfigProvider().get_api_base_url()
orderId = DataProvider().get_orderId()
clientId = DataProvider().get_clientId()
goodId = DataProvider().get_goodId()
cityId = DataProvider().get_cityId()


@allure.title("Добавление товара в корзину")
def test_add_book_in_cart():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    resp = api.add_product_in_cart(orderId, clientId, goodId)
    result = resp.json()
    with allure.step("Проверить, что id товара в корзине соответствует id добавленного товара"):
        assert result["payload"]["order"]["basket"]["items"][0]["cart"]["goodId"] == goodId
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    with allure.step("Проверить, что действие успешно"):
        assert result["success"] == True
    api.delete_product_in_cart(orderId, clientId, cityId)


@allure.title("Удаление товара из корзины")
def test_delete_book_in_cart():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    api.add_product_in_cart(orderId, clientId, goodId)
    resp = api.delete_product_in_cart(orderId, clientId, cityId)
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200


@allure.title("Изменение количества товара в корзине")
def test_increasing_product_in_cart():
    quantity = DataProvider().get_quantity()
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url)
    api.add_product_in_cart(orderId, clientId, goodId)
    resp = api.change_product_in_cart(orderId, clientId, cityId, quantity)
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    api.delete_product_in_cart(orderId, clientId, cityId)
