from random import choice
from selenium.webdriver.common.by import By
"""
## CLICK METHODS:
    1. click_random_category- clicks a random category.
    2. click_specific_category- receives a category name and goes to that category page.
"""


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    ## CLICK METHODS ##

    # clicks a random category
    def click_random_category(self):
        """
        :functionality: clicks a random category.
        :return: None
        """
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#our_products>.container>.rowSection")
        row = choice(rows)
        categories = row.find_elements(By.CSS_SELECTOR, "div>div>span")
        choice(categories).click()

    # receives a category name and goes to that category page.
    def click_specific_category(self, category_name):
        """
        :param category_name: category name.
        :fucntionality: goes to the specific category page.
        :return: None
        """
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#our_products>.container>.rowSection")
        row1_names = ['speakers', 'tablets']
        row2_names = ['laptops', 'mice', 'headphones']
        if category_name in row1_names:
            id_name = category_name + 'Img'
            category = rows[0].find_element(By.ID, id_name)
        elif category_name in row2_names:
            id_name = category_name + 'Img'
            category = rows[1].find_element(By.ID, id_name)
        else:
            print(f"Category name {category_name} not found in home page")
            return
        category.click()

