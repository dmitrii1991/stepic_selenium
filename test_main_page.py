import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.should_be_login_link()      # проверка ссылки
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # иниц. Page Object
        login_page.should_be_login_page()                     # проверка


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_items_in_cart()

