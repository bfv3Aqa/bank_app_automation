import time

from locators.add_customer_page import AddNewCustomerLocators
from pages.base_page import BasePage
from generator.generator import generated_new_customer


class AddNewCustomerPage(BasePage):
    locators = AddNewCustomerLocators()

    def add_customer(self):
        customer = next(generated_new_customer())
        self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(customer.first_name)
        self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(customer.last_name)
        self.element_is_visible(self.locators.POSTCODE_FIELD).send_keys(customer.postcode)
        self.element_is_visible(self.locators.ADD_CUSTOMER_BUTTON).click()
        time.sleep(1)
        alert_text = self.switch_to(page_type='alert_text')
        return alert_text

