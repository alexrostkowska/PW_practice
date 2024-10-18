from playwright.sync_api import Page
from locators.base_page_locators import NavbarLocators as navloc
from locators.login_page_locators import LoginLocators as loginloc

class LoginPage():
    def __init__(self,page: Page):
        self.page = page
        self.login = page.locator(navloc.LOGIN_BUTTON)
        self.username = page.locator(loginloc.USERNAME_FIELD)
        self.password = page.locator(loginloc.PASSWORD_FIELD)
        self.submit_login = page.locator(loginloc.LOGIN_BUTTON)
        self.my_account = page.locator(navloc.MY_ACCOUNT_BUTTON)
        self.logout = page.locator(navloc.LOGOUT_BUTTON)

    def navigate_to_login(self, url):
        self.page.goto(url, timeout = 5000)
        self.login.click()
    
    def fill_login_form(self, test_usr, test_pass):
        self.username = test_usr
        self.password = test_pass
    
    def login_submit_action(self):
        self.submit_login.click()

    def is_successful_login(self):
        self.my_account.is_visible()
        self.logout.is_visible()

    def is_error_message(self):
        return self.page.wait_for_selector(".error", state="visible")

