from selenium.webdriver.common.by import By


class BankManagerLocators:
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="addCust()"]')
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="openAccount()"]')
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="showCust()"]')
