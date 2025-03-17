import allure
from page.main_page import MainPage
from page.cart_page import CartPage


@allure.title("Добавление товара в корзину")
def test_add_to_cart(browser):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.new_click()
    main_page.bay_click()
    with allure.step("Перейти в корзину"):
        cart_page = CartPage(browser)
    total_product = cart_page.total_in_cart()
    with allure.step("Проверить, что товар добавлен в корзину"):
        assert total_product == "1 товар"


@allure.title("Изменение количества товара в корзине")
def test_set_to_cart(browser):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.get_product_in_cart()
    with allure.step("Перейти в корзину"):
        cart_page = CartPage(browser)
    total_product = cart_page.total_in_cart()
    with allure.step("Проверить, что товар добавлен в корзину"):
        assert total_product == "1 товар"
    cart_page.increase_product_in_cart()
    total_product = cart_page.total_in_cart()
    with allure.step("Проверить, что число товаров в корзине увеличилось"):
        assert total_product == "2 товара"


@allure.title("Удалениение товара из корзины")
def test_delete_to_cart(browser):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.get_product_in_cart()
    with allure.step("Перейти в корзину"):
        cart_page = CartPage(browser)
    total_product = cart_page.total_in_cart()
    with allure.step("Проверить, что товар добавлен в корзину"):
        assert total_product == "1 товар"
    cart_page.delete_product_in_cart()
    delete_product = cart_page.empty_cart()
    with allure.step("Проверить, что товар удален из корзины"):
        assert delete_product == "В корзине пока ничего нет"
