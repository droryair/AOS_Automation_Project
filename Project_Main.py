from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Classes.Category_Class import Category
from Classes.Homepage_Class import Homepage
from Classes.Product_Class import Product
from Classes.TopBar_Class import Topbar

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.advantageonlineshopping.com/#/")

driver.implicitly_wait(10)

homepage = Homepage(driver)
sleep(10)
homepage.click_category()

category = Category(driver)
sleep(10)
category.click_product()

product = Product(driver)
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



##r  try


sleep(3)
driver.close()


