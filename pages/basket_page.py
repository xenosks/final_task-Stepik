from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def there_are_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.any_item_in_basket), \
            "The basket is not empty"

    def text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.message_about_empty_basket), \
            "There is no message about empty page"

