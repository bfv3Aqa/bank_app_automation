from selenium.webdriver.common.by import By


class AddNewCustomerLocators:
    FIRST_NAME_FIELD = (
        By.XPATH, '//input[@ng-model="fName"]')
    LAST_NAME_FIELD = (
        By.XPATH, '//input[@ng-model="lName"]')
    POSTCODE_FIELD = (
        By.XPATH, '//input[@ng-model="postCd"]')
    ADD_CUSTOMER_BUTTON = (By.XPATH, '//button[@class="btn btn-default"]')
