from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")


class ProductPageLocators(object):
    ADD_TO_BACKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, "p.price_color")
    GOOD = (By.XPATH, "/html/body/div[2]/div/ul/li[5]")
    GOOD_BACKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class CartLocators(object):
    CART_IS_EMPTY = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    ITEMS_IN_CART = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div/h2")










