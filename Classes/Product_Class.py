from selenium.webdriver.common.by import By
"""
## IN-CLASS METHODS:
    1. is_sold_out- returns boolean value for weather an item is sold out.
## SET METHODS:
    1. set_quantity- receives a quantity int and sets the new quantity to the product
## GET METHODS:
    1. get_quantity- returns the current quantity of the product, as a string
    2. get_name- returns the product's name
    3. get_color- returns the product's color
    4. get_price- returns the product's price, as a string
## CLICK METHODS:
    1. add_to_cart- clicks 'add to cart' button
"""


class Product:
    def __init__(self, driver):
        self.driver = driver
        # self.wait3 = WebDriverWait(self.driver, 3)

    ## IN-CLASS METHODS

    # returns boolean value for weather an item is sold out.
    def is_sold_out(self):
        """
        :return: boolean value for weather an item is sold out.
        """
        sold_out_span = self.driver.find_element(By.CSS_SELECTOR, "#Description>h2>span")
        if sold_out_span.is_displayed():
            print("Product -> 23-> sold out")
            return True
        print("Product -> 25 -> not sold out")
        return False

    ##

    ## SET METHODS

    # recieves a quantity int and sets the new quantity to the product
    def set_quantity(self, quantity: int):
        """
        :param quantity: quantity int
        :functionality: sets the new quantity to the product.
        :return: None
        """
        if not self.is_sold_out():
            existing_quant = int(self.get_quantity())
            plus_btn = self.driver.find_element(By.CSS_SELECTOR, "div.plus")
            minus_btn = self.driver.find_element(By.CSS_SELECTOR, "div.minus")
            if existing_quant < quantity:
                while existing_quant < quantity:
                    plus_btn.click()
                    existing_quant = int(
                        self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value"))
            elif existing_quant > quantity:
                while existing_quant > quantity:
                    minus_btn.click()
                    existing_quant = int(
                        self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value"))

    ## GET METHODS

    # returns the current quantity of the product, as a string
    def get_quantity(self):
        """
        :return: the current quantity of the product, as a string
        """
        if not self.is_sold_out():
            existing_quant = self.driver.find_element(By.CSS_SELECTOR, "input[name=quantity]").get_attribute("value")
            return existing_quant

    # returns the product's name
    def get_name(self):
        """
        :return: the product's name
        """
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1").text

    # returns the product's color
    def get_color(self):
        """
        :return: the product's color
        """
        colors_elems = self.driver.find_elements(By.CSS_SELECTOR, "#productProperties>div>div>span")
        for color_elem in colors_elems:
            class_name = color_elem.get_attribute('class')
            if 'colorSelected' in class_name:
                return color_elem.get_attribute("title")
        print('Product -> 71 -> Error: no color selected???')

    # returns the product's price, as a string
    def get_price(self):
        """
        :return: the product's price, as a string
        """
        price_str = self.driver.find_element(By.CSS_SELECTOR, "#Description>h2").text
        return price_str

    ## CLICK METHODS

    # clicks 'add to cart' button
    def add_to_cart(self):
        """
        :functionality: clicks the 'add to cart' button
        :return: None
        """
        if not self.is_sold_out():
            btn = self.driver.find_element(By.CSS_SELECTOR, "button[name=save_to_cart]")
            btn.click()
