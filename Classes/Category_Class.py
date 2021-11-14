from random import choice

from selenium.webdriver.common.by import By


class Category:
    def __init__(self, driver):
        self.driver = driver

    def click_product(self):
        products = self.driver.find_elements(By.CSS_SELECTOR,"div.categoryRight>ul")
        choice(products).click()

