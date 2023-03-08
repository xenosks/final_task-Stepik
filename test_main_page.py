from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasePage(browser, url)
        page.open()
        page.open_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.there_are_no_items_in_basket()
        basket_page.text_about_empty_basket()

#pytest -s -m new_tests test_main_page.py
