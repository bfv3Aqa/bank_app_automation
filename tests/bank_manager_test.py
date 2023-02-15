import allure
import time
from pages.bank_manager_page import CustomersTablePage


class TestCustomersTablePage:
    def test_check_new_customer_in_table(self, driver):
        customers_table_page = CustomersTablePage(driver,
                                                  "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list")
        customers_table_page.open()
        customers_list = customers_table_page.check_new_customer()
        print(customers_list)

    def test_search_some_customer_in_table(self, driver):
        customers_table_page = CustomersTablePage(driver,
                                                  "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list")
        customers_table_page.open()
        key_word = customers_table_page.search_some_customer(key_word="Hermoine")
        customers_list = customers_table_page.check_new_customer()
        length = len(customers_list)
        assert length == 1
