import time
from selenium.webdriver import Keys

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from generator.generator import generated_customer


class BankMainPage(BasePage):
    locators = LoginPageLocators()

    def customer_login(self):
        main_button_loggin = self.element_is_visible(self.locators.CUSTOMER_LOGGIN_BUTTON).click()
        select = self.element_is_visible(self.locators.CUSTOMER_SELECT)
        select.click()
        select.send_keys(generated_customer())
        select.send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CUSTOMER_BUTTON_LOGGIN).click()
        customer_name = self.element_is_visible(self.locators.CUSTOMER_NAME_TEXT).text
        return customer_name



