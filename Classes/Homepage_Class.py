"""
homepage ('#our_products')
        optional: searchbar
"""
from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def click_product(self):
        self.driver.find_elements(By.CSS_SELECTOR)