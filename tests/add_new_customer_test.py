import allure
import time
from pages.add_customer_page import AddNewCustomerPage


class TestAddNewCustomerPage:
    def test_add_customer(self, driver):
        add_customer_page = AddNewCustomerPage(driver, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust")
        add_customer_page.open()
        text_alert = add_customer_page.add_customer()
        assert "Customer added successfully" in text_alert, "Customer added unsuccessfully"

