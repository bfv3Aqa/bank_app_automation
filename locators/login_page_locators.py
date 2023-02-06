from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGGIN_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
    BANK_MANAGER_LOGIN = (By.CSS_SELECTOR, 'button[ng-click="manager()"]')
    CUSTOMER_SELECT = (By.CSS_SELECTOR, 'select[id="userSelect"]')
    CUSTOMER_BUTTON_LOGGIN = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')
    CUSTOMER_NAME_TEXT = (By.CSS_SELECTOR, 'span[class="fontBig ng-binding"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'button[class="btn logout"]')
    HOME_BUTTON = (By.CSS_SELECTOR, 'button[class="btn home"]')
