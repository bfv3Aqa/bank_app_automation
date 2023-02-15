from selenium.webdriver.common.by import By


class LkPageLocators:
    CURRENCY_SELECT = (By.XPATH, '//select[@id="accountSelect"]]')
    ACCOUNT_NUMBER_LABEL = (By.XPATH, '//strong[@class="ng-binding"][1]')
    ACCOUNT_BALANCE_LABEL = (By.XPATH, '//button[@ng-click="manager()"]')
    CURRENCY_LABEL = (By.XPATH, '//strong[@class="ng-binding"][3]')

    TRANSACTIONS_BUTTON = (By.XPATH, '//button[@ng-class="btnClass1"]')
    DEPOSIT_BUTTON = (By.XPATH, '//button[@ng-class="btnClass2"]')
    WITHDRAWL_BUTTON = (By.XPATH, '//button[@ng-class="btnClass3"]')

    DEPOSIT_AND_WITHDRAWL_AMOUT_LABEL = (By.XPATH, '//input[@ng-model="amount"]')
    DEPOSIT_AND_WITHDRAWL_SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')