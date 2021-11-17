"""
product (choose quantity, add to cart)
"""
from random import choice
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Product:
    def __init__(self, driver):
        self.driver = driver
        # self.wait3 = WebDriverWait(self.driver, 3)

    ## in-class methods:

    def is_sold_out(self):
        sold_out_span = self.driver.find_element(By.CSS_SELECTOR, "#Description>h2>span")
        if sold_out_span.is_displayed():
            print("Product -> 23-> sold out")
            return True
        print("Product -> 25 -> not sold out")
        return False

    ##

    def change_quantity(self, quantity):
        if not self.is_sold_out():
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

    def get_quantity(self):
        if not self.is_sold_out():
            existing_quant = self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value")
            return existing_quant
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

    def get_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1").text

    def get_color(self):
        # class include('colorSelected')
        colors_elems = self.driver.find_elements(By.CSS_SELECTOR, "#productProperties>div>div>span")
        for color_elem in colors_elems:
            class_name = color_elem.get_attribute('class')
            if 'colorSelected' in class_name:
                return color_elem.get_attribute("title")
        print('Product -> 71 -> Error: no color selected???')

    def get_price(self):
        ## Descritopn>h2.text
        price_str = self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text
        return price_str

    def add_to_cart(self):
        if not self.is_sold_out():
            btn = self.driver.find_element(By.CSS_SELECTOR, "button[name=save_to_cart]")
            btn.click()



