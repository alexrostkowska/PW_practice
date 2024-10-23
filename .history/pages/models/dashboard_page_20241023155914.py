from itertools import count
from playwright.sync_api import Page, expect

from locators.base_page_locators import TableLocators as tabloc
from locators.base_page_locators import NavbarLocators as navloc
import re

class DashboardPage():
    def __init__(self, page: Page):
        self.table = page.locator(tabloc.PRODUCT_TABLE)
        self.filter_field = page.locator(tabloc.FILTER_TABLE)
        self.filter_button = page.locator(tabloc.FILTER_BUTTON)
        self.filter_reset = page.locator(tabloc.FILTER_RESET_BUTTON)
        self.table_rows = page.locator(tabloc.TABLE_ROWS)
        self.add_product = page.locator(navloc.ADD_PRODUCT_BUTTON)

    def is_product_table(self):
        expect(self.table).to_be_visible()
        
        #check that table is not empty

    def is_filter_table(self):
        self.filter_field.fill("Product 1")
        self.filter_button.click()
        expect(self.table_rows).to_have_count(5)

    def is_reset_filter(self):
        self.filter_reset.click()
        expect(self.table_rows).not_to_have_count(5)
    
    def is_add_product(self, page: Page):
        #click add product
        self.page.goto(baseurl)
        self.add_product.click()
        expect(page).to_have_url(re.compile(r".*/addproduct"))
        #fill form
        #submit form
        #check that product is in table
        #check that product is in database