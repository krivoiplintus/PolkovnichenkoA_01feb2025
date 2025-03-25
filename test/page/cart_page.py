import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configyration.config_provider import ConfigProvider


class CartPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get_ui_url_cart_page()
        self.__driver = driver
        self.__driver.get(self.__url)
        self.__driver.fullscreen_window()

    @allure.step("Узнать количество товаров в корзине")
    def total_in_cart(self) -> str:
        return self.__driver.find_element(By.CSS_SELECTOR, 'div.GoodsBlock-module__count--WC7jV').text

    @allure.step("Увеличить количество товара")
    def increase_product_in_cart(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'button[data-testid="addition-id"]').click()

    @allure.step("Удалить товар")
    def delete_product_in_cart(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, 'button.CheckoutCard-module__deleteButton--JlUTL').click()

    @allure.step("Проверить, что корзина пуста")
    def empty_cart(self) -> str:
        return self.__driver.find_element(By.CSS_SELECTOR, 'div.CorgiBlock-module__title--miiZy.Title-module__title--lh3ei.Title-module__h3--serax.Title-module__default--aVCoc.Title-module__wide--sz3iM').text
