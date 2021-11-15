from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Classes.Cart_Class import Cart
from Classes.Category_Class import Category
from Classes.Homepage_Class import Homepage
from Classes.Product_Class import Product
from Classes.TopBar_Class import Topbar

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.advantageonlineshopping.com/#/")

driver.implicitly_wait(10)
driver.maximize_window()


# this function will receive a string and turn it into a number (int/float)
def str_to_num(stri: str):
    """
    :param stri: string including numeric characters and no more than one dot (.)
    :return: that string as a number type (int/float), depends on the existence of a dot (.)
    """
    is_float = False
    for char in stri:
        if not char.isnumeric():
            if char == '.':
                is_float = True
                continue
            stri = stri.replace(char, '')
    if is_float:
        return float(stri)
    return int(stri)


homepage = Homepage(driver)
sleep(10)
homepage.click_category()

category = Category(driver)
sleep(10)
category.click_product()

product = Product(driver)
sleep(1)
product.change_quantity(2)
product.add_to_cart()

topbar = Topbar(driver)
topbar.click_aos_logo()

homepage.click_category()
sleep(1)
category.click_product()
sleep(1)
product.change_quantity(3)
product.add_to_cart()
topbar.click_cart()

cart = Cart(driver)
sleep(3)
quantities_str = cart.get_products_quantities()
print("quantities: ", quantities_str)
names = cart.get_products_names()
print("names: ", names)
colors = cart.get_products_colors()
print("colors: ", colors)
prices_str = cart.get_products_price()
prices_num = []
for price_str in prices_str:
    num_price = str_to_num(price_str)
    prices_num.append(num_price)
    print("type num_price", type(num_price))
print("prices_str: ", prices_str)
print("prices_num: ", prices_num)





##r  try


sleep(3)
driver.close()


