from playwright.sync_api import Page

from pages.locators.base_page_locators import NavbarLocators as navloc

class AccountPage():
    def __init__(self, page: Page):
        super().__init__(page)
        self.my_account = page.locator(navloc.LOGIN_BUTTON)

    def is_my_account_contains(self, value):
        if self.my_account.find(value) == -1:
            return False
        else:
            return True