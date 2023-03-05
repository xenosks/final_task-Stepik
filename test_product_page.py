from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_correct_product()
    page.is_price_correct()



#pytest -s test_product_page.py

