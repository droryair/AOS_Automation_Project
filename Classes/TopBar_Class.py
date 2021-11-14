"""
top bar (user, cart)
"""
from selenium.webdriver.common.by import By


class Topbar:
    def __init__(self, driver):
        self.driver = driver
        self.user_btn = self.driver.find_element(By.ID,"menuUserLink")

    def click_cart(self):
        cart = self.driver.find_element(By.ID,"menuCart")
        cart.click()

    def click_my_account(self):
        self.user_btn.click()
        my_account = self.driver.find_element(By.LINK_TEXT,"My account")
        my_account.click()

    def click_my_orders(self):
        self.user_btn.click()
        my_orders = self.driver.find_element(By.LINK_TEXT,"My orders")
        my_orders.click()

    def click_sign_out(self):
        self.user_btn.click()
        sign_out = self.driver.find_element(By.LINK_TEXT,"Sign out")
        sign_out.click()

    def click_aos_logo(self):
        aos_logo = self.driver.find_element(By.CSS_SELECTOR, "a[href='#/']")
        aos_logo.click()