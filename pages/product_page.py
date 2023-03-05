from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.basket)
        basket.click()

    def is_correct_product(self):
        product_message = self.browser.find_element(*ProductPageLocators.message_for_product)
        message = product_message.text
        name_of_the_book = self.browser.find_element(*ProductPageLocators.book_name)
        book = name_of_the_book.text
        assert book in message, "The book name is incorrect"

    def is_price_correct(self):
        price_message = self.browser.find_element(*ProductPageLocators.message_for_price)
        the_message = price_message.text
        correct_price = self.browser.find_element(*ProductPageLocators.price)
        the_price = correct_price.text
        assert the_price == the_message, "The price is incorrect"
