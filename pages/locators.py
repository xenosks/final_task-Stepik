from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket_link = (By.CSS_SELECTOR, ".basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")
    email_input = (By.CSS_SELECTOR, "#id_registration-email")
    password_input1 = (By.CSS_SELECTOR, "#id_registration-password1")
    password_input2 = (By.CSS_SELECTOR, "#id_registration-password2")
    register_button = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    basket = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    message_for_product = (By.CSS_SELECTOR, "div.alertinner ")
    book_name = (By.CSS_SELECTOR, "div.product_main h1")
    message_for_price = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    price = (By.CSS_SELECTOR, ".product_main .price_color")
    message_of_success = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators():
    any_item_in_basket = (By.CSS_SELECTOR, "#basket_formset")
    message_about_empty_basket = (By.XPATH, '//div[@id="content_inner"]//p')