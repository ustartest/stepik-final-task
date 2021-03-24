# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()

    def solve_quiz_and_get_code(self):
        return BasePage.solve_quiz_and_get_code(self)

    def product_added_to_cart_message_exist(self):
        assert BasePage.is_element_present(self, *ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Product added to cart message not visible"

    def cart_message_contain_product_title(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text == \
               self.browser.find_element(*ProductPageLocators.CART_PRODUCT_TITLE).text, \
               "Cart message not contain product title"

    def cart_price_message_exist(self):
        assert BasePage.is_element_present(self, *ProductPageLocators.CART_PRICE_MESSAGE), \
            "Cart price message not visible"

    def cart_price_contain_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.CART_PRICE).text, "Cart price not contain product price"
