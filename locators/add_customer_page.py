from selenium.webdriver.common.by import By


class AddNewCustomerLocators:
    FIRST_NAME_FIELD = (
        By.CSS_SELECTOR, 'input[ng-model="fName"]')
    LAST_NAME_FIELD = (
        By.CSS_SELECTOR, 'input[ng-model="lName"]')
    POSTCODE_FIELD = (
        By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')


class CustomersTableLocators:
    SEARCH_FILED = (
        By.CSS_SELECTOR, 'input[class="form-control ng-pristine ng-untouched ng-valid"]')
    # FIRST_NAME_SORT_LINK = (By.CSS_SELECTOR, 'a[ng-click="sortType = 'fName'; sortReverse = !sortReverse"]')
    DELETE_CUSTOMER_BUTTON = (By.CSS_SELECTOR, 'button[ng-click="deleteCust(cust)"]')