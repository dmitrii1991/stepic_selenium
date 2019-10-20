from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
# from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_backet(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BACKET_BUTTON), "not backet button"
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKET_BUTTON)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")