import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://commitquality.com/")

    # [data-testid = 'navbar-login']
    # expect("[data-testid = 'navbar-login']").to_be_visible()
    page.click("[data-testid = 'navbar-login']")
    # expect(page).to_have_url(re.compile(r".*/login"))
    expect(page).to_have_url("https://commitquality.com/login")
    expect("[data-testid = 'username-textbox']").to_be_visible()
    expect("[data-testid = 'username-textbox']").fill("test")
    expect("[data-testid = 'password-textbox']").fill("test")
    page.click("[data-testid = 'login-button']")
    expect("[data-testid = 'navbar-account']").to_be_visible()
    expect("[data-testid = 'navbar-logout']").to_be_visible()

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()