# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main>h1")
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    CART_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
