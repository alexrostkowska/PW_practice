import pytest
from playwright.sync_api import Page 
from models.dashboard_page import DashboardPage

def test_table_display(page: Page, pytestconfig: pytest.Config):
    base_url = pytestconfig.getini('base_url')

    main_page = DashboardPage(page)
    page.goto(base_url)

    main_page.is_product_table()

def test_filter_table(page: Page, pytestconfig: pytest.Config):
    base_url = pytestconfig.getini('base_url')

    main_page = DashboardPage(page)
    page.goto(base_url)

    main_page.is_filter_table()

    main_page.is_reset_filter()

def test_add_product(main_page: DashboardPage, page: Page):
    main_page.is_add_product(page)
    # main_page.is_product_in_table(page)
    # main_page.is_product_in_database(page)
