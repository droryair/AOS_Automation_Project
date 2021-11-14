"""
product (choose quantity, add to cart)
"""
from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver):
        self.driver = driver