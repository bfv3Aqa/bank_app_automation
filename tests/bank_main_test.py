import allure
import time
from pages.bank_main_page import BankMainPage


class TestBankMainPage:
    def test_customer_login(self, driver):
        login_page = BankMainPage(driver, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        login_page.open()
        customer_name = login_page.customer_login()
        print(customer_name)
        assert customer_name in ["Hermoine Granger", "Harry Potter", "Ron Weasly", "Albus Dumbledore",
                                 "Neville Longbottom"]
        time.sleep(3)
