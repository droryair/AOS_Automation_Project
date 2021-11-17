from random import choice
from selenium.webdriver.common.by import By

"""
1. click_random_product - clicks a random product in the page.
"""

class Category:
    def __init__(self, driver):
        self.driver = driver

    #clicks a random product in the page
    def click_random_product(self):
        """
        :functionality: clicks a random product in the page
        :return: None
        """
        products = self.driver.find_elements(By.CSS_SELECTOR, "div.categoryRight>ul>li")
        choice(products).click()

