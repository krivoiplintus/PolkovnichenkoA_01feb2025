import allure
import requests


class CompanyApi:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    @allure.step("Добавить товар в корзину")
    def add_product_in_cart(self, orderId: int, clientId: int, goodId: int) -> requests.Response:
        body = {
            "context": {
                "branchId": 615, "orderId": orderId, "clientId": clientId
                },
            "operations": [{"operation": "OrderAddGoodToBasket", "arguments": {"goodId": goodId, "quantity": 1}}]
            }
        responses = requests.post(self.base_url + "batch/order", json=body)
        return responses

    @allure.step("Удалить товар из корзины")
    def delete_product_in_cart(self, orderId: int, clientId: int, cityId: int) -> requests.Response:
        responses = requests.delete(self.base_url + "order/" + str(orderId) + "/basket/1/remove", headers={"clientId": str(clientId), "cityId": str(cityId)})
        return responses

    @allure.step("Изменить количество товара в корзине")
    def change_product_in_cart(self, orderId: int, clientId: int, cityId: int, quantity: int) -> requests.Response:
        body = {"quantity": quantity}
        responses = requests.patch(self.base_url + "order/" + str(orderId) + "/basket/1/quantity", json=body, headers={"clientId": str(clientId), "cityId": str(cityId)})
        return responses
