from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
2. click_specific_product- receives an id number and clicks the product matching that id.
"""

class Category:
    def __init__(self, driver):
        self.driver = driver
        self.wait10 = WebDriverWait(self.driver, 10)

    # receives an id number and clicks the product matching that id
    def click_specific_product(self, id):
        """
        :param id: product's id number
        :functionality: clicks the  product matching the given id
        :return: None
        """
        # waiting for the page to load:
        self.wait10.until(EC.visibility_of((self.driver.find_element(By.CLASS_NAME, "categoryRight"))))
        product_elem = self.driver.find_element(By.CSS_SELECTOR, f"img[id='{id}']")
        product_elem.click()

