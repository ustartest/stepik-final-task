# -*- coding: utf-8 -*-

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_added_to_cart_message_exist()
    page.cart_message_contain_product_title()
    page.cart_price_message_exist()
    page.cart_price_contain_product_price()
