"""
cart (quantity, name, color, price, remove, "shopping cart" text, Total)
"""
from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
        self.driver = driver