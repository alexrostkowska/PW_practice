import pytest
from playwright.sync_api import Page 
from models.login_page import LoginPage

# def test_has_title(page: Page):
#     page.goto("https://commitquality.com/")

#     # [data-testid = 'navbar-login']
#     # expect("[data-testid = 'navbar-login']").to_be_visible()
#     page.click()
#     expect(page).to_have_url(re.compile(r".*/login"))
#     page.locator("[data-testid = 'username-textbox']").fill("test")
#     page.locator("[data-testid = 'password-textbox']").fill("test")
#     page.click("[data-testid = 'login-button']")
#     page.locator("[data-testid = 'navbar-account']").is_visible()
#     page.locator("[data-testid = 'navbar-logout']").is_visible()

def test_successful_login(page: Page, pytestconfig: pytest.Config):
    base_url = pytestconfig.getini('base_url')

    login_page = LoginPage(page)
    login_page.navigate_to_login(base_url)

    login_page.fill_login_form("test", "test")
    login_page.login_submit_action()

    login_page.is_successful_login()
