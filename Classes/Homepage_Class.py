"""
homepage ('#our_products')
        optional: searchbar
"""
from random import choice
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def click_random_category(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR,"#our_products>.container>.rowSection")
        row = choice(rows)
        categories = row.find_elements(By.CSS_SELECTOR, "div>div>span")
        choice(categories).click()

    def click_specific_category(self, category_name):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#our_products>.container>.rowSection")
        row1_names = ['speakers', 'tablets']
        row2_names = ['laptops', 'mice', 'headphones']
        if category_name in row1_names:
            id_name = category_name + 'Img'
            # category = rows[0].find_element(By.ID, id_name)
            category = rows[0].find_element(By.CSS_SELECTOR, f"div[id={id_name}]")
        elif category_name in row2_names:
            id_name = category_name + 'Img'
            # category = rows[1].find_element(By.ID, id_name)
            category = rows[1].find_element(By.CSS_SELECTOR, f"div[id={id_name}]")
        else:
            print(f"Category name {category_name} not found in home page")
            return
        category.click()
        # names = speakers/ tablets/ laptops/ mice /headphones



if __name__ == '__main__':
    service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.advantageonlineshopping.com/#/")

    driver.implicitly_wait(10)

    homepage = Homepage(driver)
    homepage.click_category()
