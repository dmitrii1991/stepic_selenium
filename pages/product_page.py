from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_backet(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BACKET_BUTTON), "not backet button"
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKET_BUTTON)
        link.click()

    def correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_check = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price == price_check, "Price wrong"

    def correct_item(self):
        item = self.browser.find_element(*ProductPageLocators.GOOD).text
        items_check = self.browser.find_element(*ProductPageLocators.GOOD_BACKET).text
        assert item == items_check, "Wrong item"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"