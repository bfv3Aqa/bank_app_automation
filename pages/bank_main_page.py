import time
from selenium.webdriver import Keys

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from generator.generator import generated_customer


class BankMainPage(BasePage):
    locators = LoginPageLocators()

    def customer_login(self):
        self.element_is_visible(self.locators.CUSTOMER_LOGGIN_BUTTON).click()
        select = self.element_is_visible(self.locators.CUSTOMER_SELECT)
        select.click()
        select.send_keys(generated_customer())
        select.send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CUSTOMER_BUTTON_LOGGIN).click()
        customer_name = self.element_is_visible(self.locators.CUSTOMER_NAME_TEXT).text
        return customer_name

    def customer_logout(self):
        self.element_is_visible(self.locators.LOGOUT_BUTTON).click()
        self.element_is_visible(self.locators.HOME_BUTTON).click()
        if self.element_is_visible(self.locators.CUSTOMER_LOGGIN_BUTTON):
            return True
        else:
            return False

    def home_button_usage(self):
        self.element_is_visible(self.locators.HOME_BUTTON).click()
        url = self.driver.current_url
        return url



