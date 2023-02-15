from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGGIN_BUTTON = (By.XPATH, '//button[@ng-click="customer()"]')
    BANK_MANAGER_LOGIN = (By.XPATH, '//button[@ng-click="manager()"]')
    CUSTOMER_SELECT = (By.XPATH, '//select[@id="userSelect"]')
    CUSTOMER_BUTTON_LOGGIN = (By.XPATH, '//button[@class="btn btn-default"]')
    CUSTOMER_NAME_TEXT = (By.XPATH, '//span[@class="fontBig ng-binding"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="btn logout"]')
    HOME_BUTTON = (By.XPATH, '//button[@class="btn home"]')

