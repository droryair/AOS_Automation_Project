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
from Classes.MyOrders_Class import MyOrders
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
sleep(3)
homepage.click_random_category()

category = Category(driver)
sleep(3)
category.click_product()

product = Product(driver)
sleep(1)
product.change_quantity(2)
product.add_to_cart()

topbar = Topbar(driver)
topbar.click_aos_logo()

homepage.click_random_category()
sleep(1)
category.click_product()
sleep(1)
product.change_quantity(3)
product.add_to_cart()
topbar.click_cart()

sleep(5)
cart = Cart(driver)
quantities_str = cart.get_products_quantities()
names = cart.get_products_names()
colors = cart.get_products_colors()
prices_str = cart.get_products_price()
# print("quantities: ", quantities_str)
# print("names: ", names)
# print("colors: ", colors)
# print("prices_str: ", prices_str)


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
create_account.set_username('NewUser1234')
create_account.set_password('Pa55w.rd', True)
create_account.set_email('something@try.abc')
sleep(3)
create_account.check_i_agree()
sleep(0.5)
create_account.click_register()
sleep(5)
try:
    order_payment.click_next()
except:
    print("user already exists")

sleep(3)
order_payment.set_safepay_username('SafeUser123')
order_payment.set_safepay_password('SafePay1234')
order_payment.click_pay_now()
sleep(1)

order_number = order_payment.get_order_number()
print("first order number: ", order_number)

topbar.click_cart()
sleep(3)
print(cart.is_cart_empty())

topbar.click_my_orders()
# topbar.click_menu_item(1)
my_orders = MyOrders(driver)
orders_numbers = my_orders.get_orders_numbers()
print("all orders numbers", orders_numbers)

if order_number in orders_numbers:
    print(f"The order {order_number} was added to the 'My Orders' page. (existing orders:{orders_numbers})")
else:
    print(f"The order: {order_number} was NOT added to the 'My Orders' page. (existing orders:{orders_numbers})")

str_total_orders_costs = my_orders.get_total_orders_costs()
total_orders_costs=[]
for string in str_total_orders_costs:
    total_orders_costs.append(str_to_num(string))

print("total_orders_costs: ", total_orders_costs)


def delete_user():
    topbar.click_my_account()
    delete_account_btn = driver.find_element(By.CSS_SELECTOR, "#myAccountContainer>div>button")
    delete_account_btn.click()
    sleep(0.5)



##r  try

sleep(3)
delete_user()



