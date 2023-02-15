from pages.lk_page import LkPage


class TestLkPage:
    def test_something(self, driver):
        lk_page = LkPage(driver, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account")
        lk_page.open()
