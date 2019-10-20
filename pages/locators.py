from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class  LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REG_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password2")















