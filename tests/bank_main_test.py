import allure
import time
from pages.bank_main_page import BankMainPage


class TestBankMainPage:
    def test_customer_login(self, driver):
        login_page = BankMainPage(driver, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        login_page.open()
        time.sleep(3)