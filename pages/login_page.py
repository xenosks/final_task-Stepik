from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is incorrect link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "There is no register form"

    def register_new_user(self, email, password):
        self.should_be_login_page()
        self.browser.find_element(*LoginPageLocators.email_input).send_keys(email)
        self.browser.find_element(*LoginPageLocators.password_input1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.password_input2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.register_button).click()


        