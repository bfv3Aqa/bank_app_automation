from selenium.webdriver.common.by import By


class AddNewCustomerLocators:
    FIRST_NAME_FIELD = (
        By.CSS_SELECTOR, 'input[class="form-control ng-pristine ng-invalid ng-invalid-required ng-touched"]')
    LAST_NAME_FIELD = (
        By.CSS_SELECTOR, 'input[class="form-control ng-pristine ng-untouched ng-invalid ng-invalid-required"]')
    POSTCODE = (By.CSS_SELECTOR, 'input[class="form-control ng-pristine ng-untouched ng-invalid ng-invalid-required"]')
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')