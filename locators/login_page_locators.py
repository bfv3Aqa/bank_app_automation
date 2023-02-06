from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGGIN_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
    BANK_MANAGER_LOGIN = (By.CSS_SELECTOR, 'button[ng-click="manager()"]')
    CUSTOMER_SELECT = (By.CSS_SELECTOR, 'select[id="userSelect"]')
