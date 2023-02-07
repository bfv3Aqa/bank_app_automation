from selenium.webdriver.common.by import By


class AddNewCustomerLocators:
    FIRST_NAME_FIELD = (
        By.CSS_SELECTOR, 'input[ng-model="fName"]')
    LAST_NAME_FIELD = (
        By.CSS_SELECTOR, 'input[ng-model="lName"]')
    POSTCODE_FIELD = (
        By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')
