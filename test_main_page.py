from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_link()      # проверка ссылки
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

    login_page = LoginPage(browser, browser.current_url)  # иниц. Page Object
    login_page.should_be_login_page()                     # проверка


