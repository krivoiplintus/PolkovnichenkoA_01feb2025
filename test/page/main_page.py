import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from configyration.config_provider import ConfigProvider


class MainPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get_ui_url_main_page()
        self.__driver = driver
        self.__driver.get(self.__url)
        self.__driver.fullscreen_window()

    @allure.step("Кликнуть по кнопке купить")
    def bay_click(self):
        self.__driver.fullscreen_window()
        self.__driver.implicitly_wait(5)
        self.__driver.find_element(By.CSS_SELECTOR, 'div.b-good__buy.buyBut').click()
        self.__driver.implicitly_wait(10)
        self.__driver.find_element(By.CSS_SELECTOR, 'div.RecommendationsModal-module__controls--Nz5i3')

    @allure.step("Кликнуть раздел новинки")
    def new_click(self) -> None:
        element = self.__driver.find_elements(By.CSS_SELECTOR, '[href="/mobile/-new_goods"]')
        element[1].click()

    @allure.step("Добавить товар в корзину")
    def get_product_in_cart(self) -> None:
        element = self.__driver.find_elements(By.CSS_SELECTOR, '[href="/mobile/-new_goods"]')
        element[1].click()
        self.__driver.fullscreen_window()
        self.__driver.implicitly_wait(5)
        self.__driver.find_element(By.CSS_SELECTOR, 'div.b-good__buy.buyBut').click()
        self.__driver.implicitly_wait(10)
        self.__driver.find_element(By.CSS_SELECTOR, 'div.RecommendationsModal-module__controls--Nz5i3')
