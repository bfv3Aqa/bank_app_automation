import time

from locators.bank_manager_page_locators import CustomersTableLocators
from pages.base_page import BasePage


class CustomersTablePage(BasePage):
    locators = CustomersTableLocators()

    def check_new_customer(self):
        customers_list = self.elements_are_present(self.locators.FULL_CUSTOMERS_LIST)
        data = []
        for item in customers_list:
            data.append(item.text.splitlines())
        return data

    def search_some_customer(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FILED).send_keys(key_word)
        return key_word

    def delete_customer_from_table(self):
        pass
