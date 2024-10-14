import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://commitquality.com/")

    # [data-testid = 'navbar-login']
    # expect("[data-testid = 'navbar-login']").to_be_visible()
    page.click("[data-testid = 'navbar-login']")
    expect(page).to_have_url(re.compile(r".*/login"))
    page.locator("[data-testid = 'username-textbox']").fill("test")
    page.locator("[data-testid = 'password-textbox']").fill("test")
    page.click("[data-testid = 'login-button']")
    page.locator("[data-testid = 'navbar-account']").is_visible()
    page.locator("[data-testid = 'navbar-logout']").is_visible()

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()