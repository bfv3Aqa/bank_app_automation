from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class BankMainPage(BasePage):
    locators = LoginPageLocators()

    def customer_login(self):
        pass
