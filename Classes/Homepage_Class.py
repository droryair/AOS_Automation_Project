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

    def click_category(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR,"#our_products>.container>.rowSection")
        row = choice(rows)
        categories = row.find_elements(By.CSS_SELECTOR, "div>div>span")
        choice(categories).click()



if __name__ == '__main__':
    service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.advantageonlineshopping.com/#/")

    driver.implicitly_wait(10)

    homepage = Homepage(driver)
    homepage.click_category()
