from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
## Delete
from selenium.webdriver.common.by import By
##

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Classes.Cart_Class import Cart
from Classes.Category_Class import Category
from Classes.CreateAccount_Class import CreateAccount
from Classes.Homepage_Class import Homepage
from Classes.OrderPayment_Class import OrderPayment
from Classes.Product_Class import Product
from Classes.TopBar_Class import Topbar

service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.advantageonlineshopping.com/#/")

driver.implicitly_wait(10)
driver.maximize_window()
wait10 = WebDriverWait(driver, 10)
wait3 = WebDriverWait(driver, 3)

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

sleep(10)
cart = Cart(driver)
quantities_str = cart.get_products_quantities()
names = cart.get_products_names()
colors = cart.get_products_colors()
prices_str = cart.get_products_price()
print("quantities: ", quantities_str)
print("names: ", names)
print("colors: ", colors)
print("prices_str: ", prices_str)


def price_str_to_num():
    prices_num = []
    for price_str in prices_str:
        num_price = str_to_num(price_str)
        prices_num.append(num_price)
    return prices_num


print("prices_num: ", price_str_to_num())

cart.click_checkout()

sleep(3)
order_payment = OrderPayment(driver)
order_payment.click_registration()

create_account = CreateAccount(driver)
sleep(3)
create_account.set_username('NewUser123')
create_account.set_password('Pa55w.rd', True)
create_account.set_email('something@try.abc')
sleep(3)
create_account.check_i_agree()
sleep(0.5)
create_account.click_register()

order_payment.click_next()

def delete_user():
    topbar.click_my_account()
    delete_account_btn = driver.find_element(By.CSS_SELECTOR,"#myAccountContainer>div>button")
    delete_account_btn.click()
    sleep(0.5)
    yes_btn = driver.find_element(By.LINK_TEXT, "yes")
    yes_btn.click()


##r  try

delete_user()
sleep(3)
driver.close()


