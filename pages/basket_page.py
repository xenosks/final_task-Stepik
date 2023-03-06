import pytest
from final_task_Stepik.pages.base_page import BasePage
from final_task_Stepik.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def there_are_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.any_item_in_basket), "The basket is not empty"

    def text_about_empty_basket(self):
        text_about_empty_basket = self.browser.find_element(*BasketPageLocators.message_about_empty_basket)
        is_text_correct = text_about_empty_basket.text
        assert "Your basket is empty" in is_text_correct, "There is no message about empty page"

