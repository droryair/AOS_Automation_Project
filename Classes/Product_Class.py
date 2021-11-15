"""
product (choose quantity, add to cart)
"""
from random import choice
from time import sleep

from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver):
        self.driver = driver

    def change_quantity(self, quantity):
        # clear() and send_keys() didn't work. using buttons:
        existing_quant = int(self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value"))
        plus_btn = self.driver.find_element(By.CSS_SELECTOR, "div.plus")
        minus_btn = self.driver.find_element(By.CSS_SELECTOR, "div.minus")
        # existing_quant.send_keys(quantity)
        if existing_quant < quantity:
            while existing_quant < quantity:
                plus_btn.click()
                existing_quant = int(self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value"))
        elif existing_quant > quantity:
            while existing_quant > quantity:
                minus_btn.click()
                existing_quant = int(self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value"))

    '''    
    def choose_random_color(self):
        ##   #productProperties>div[class='colors ng-scope']>div:nth-child(3)>span
        ## //div[@id='productProperties']/div[@class='colors ng-scope']/div[2]/span
        colors = self.driver.find_elements(By.XPATH, "//div[@id='productProperties']/div[@class='colors ng-scope']/div[@ng-show='!firstImageToShow']/span")
                                                     #//div[@id='productProperties']/div[@class='colors ng-scope']/div[2]/span")
        print("choose_random_color-> type colors", type(colors))
        one_color = choice(colors)
        one_color.click()
        # print("one_color", one_color)
    '''

    def add_to_cart(self):
        btn = self.driver.find_element(By.CSS_SELECTOR,"button[name=save_to_cart]")
        btn.click()
