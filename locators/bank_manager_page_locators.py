from selenium.webdriver.common.by import By


class BankManagerLocators:
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="addCust()"]')
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="openAccount()"]')
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="showCust()"]')


class CustomersTableLocators:
    FULL_CUSTOMERS_LIST = (
        By.CSS_SELECTOR, 'tr[ng-repeat="cust in Customers | orderBy:sortType:sortReverse | filter:searchCustomer"]')
    SEARCH_FILED = (
        By.CSS_SELECTOR, 'input[class="form-control ng-pristine ng-untouched ng-valid"]')
    # FIRST_NAME_SORT_LINK = (By.CSS_SELECTOR, 'a[ng-click="sortType = 'fName'; sortReverse = !sortReverse"]')
    DELETE_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="deleteCust(cust)"]')