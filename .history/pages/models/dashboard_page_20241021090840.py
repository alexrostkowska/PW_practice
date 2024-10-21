from playwright.sync_api import Page, expect

from locators.base_page_locators import TableLocators as tabloc

class DashboardPage():
    def __init__(self, page: Page):
        self.table = page.locator(tabloc.PRODUCT_TABLE)
        self.filter_field = page.locator(tabloc.FILTER_TABLE)
        self.filter_button = page.locator(tabloc.FILTER_BUTTON)
        self.filter_reset = page.locator(tabloc.FILTER_RESET_BUTTON)

    def is_product_table(self):
        expect(self.table).to_be_visible()
        
        #check that table is not empty

    def is_filter_table(self):
        self.filter_field.fill("Product 1")
        self.filter_button.click()
        tr = self.table.get_by_role
        if len(tr) == 5:
            return True
        else:
            return False

