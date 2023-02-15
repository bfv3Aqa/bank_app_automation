from pages.base_page import BasePage
from locators.lk_page_locators import LkPageLocators


class LkPage(BasePage):
    locators = LkPageLocators()

    def test(self):
        pass