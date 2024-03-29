import pytest
import time

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage


@pytest.mark.user_can_add
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        email = f"{time.time()}@1111111.test"
        password = "11111111111111"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        cart = ProductPage(browser, link)
        cart.open()
        cart.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        cart = ProductPage(browser, link)
        cart.open()
        cart.add_to_backet()
        cart.correct_price()
        cart.correct_item()

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_backet()
    cart.correct_price()
    cart.correct_item()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    c_page = CartPage(browser, browser.current_url)
    c_page.cart_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    login = LoginPage(browser, link)
    login.open()
    login.go_to_login_page()
    login.should_be_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_backet()
    cart.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_backet()
    cart.should_be_disappeared_success_message()
