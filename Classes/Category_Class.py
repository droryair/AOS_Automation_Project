from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
1. click_random_product - clicks a random product in the page.
"""

class Category:
    def __init__(self, driver):
        self.driver = driver
        self.wait10 = WebDriverWait(self.driver, 10)

    #clicks a random product in the page
    def click_random_product(self):
        """
        :functionality: clicks a random product in the page
        :return: None
        """
        self.wait10.until(EC.visibility_of((self.driver.find_element(By.CLASS_NAME, "categoryRight"))))
        products = self.driver.find_elements(By.CSS_SELECTOR, "div.categoryRight>ul>li")
        choice(products).click()

