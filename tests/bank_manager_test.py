import allure
import time
from pages.bank_manager_page import CustomersTablePage
from generator.generator import generated_customer


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
        customer_name_for_search = generated_customer()
        customer_name_for_search = customer_name_for_search.split(" ")
        print(customer_name_for_search)
        key_word = customers_table_page.search_some_customer(key_word=customer_name_for_search[0])
        customers_list = customers_table_page.check_new_customer()
        assert key_word in str(customers_list), "Customer was not found"

    def test_delete_customer(self, driver):
        customers_table_page = CustomersTablePage(driver,
                                                  "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list")
        customers_table_page.open()
        customer = customers_table_page.delete_customer_from_table()
        print(customer)