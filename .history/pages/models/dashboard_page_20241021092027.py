from itertools import count
from playwright.sync_api import Page, expect

from locators.base_page_locators import TableLocators as tabloc

class DashboardPage():
    def __init__(self, page: Page):
        self.table = page.locator(tabloc.PRODUCT_TABLE)
        self.filter_field = page.locator(tabloc.FILTER_TABLE)
        self.filter_button = page.locator(tabloc.FILTER_BUTTON)
        self.filter_reset = page.locator(tabloc.FILTER_RESET_BUTTON)
        self.table_rows = page.locator(tabloc.TABLE_ROWS)

    def is_product_table(self):
        expect(self.table).to_be_visible()
        
        #check that table is not empty

    def is_filter_table(self):
        self.filter_field.fill("Product 1")
        self.filter_button.click()
        expect(self.table_rows).to_have_count(5)

    def is_reset_filter(self):
        self.filter_reset.click()
        expect(self.table_rows).to_have_count(5)
