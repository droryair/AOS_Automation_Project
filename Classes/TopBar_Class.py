"""
top bar (user, cart)
"""
## delete
from time import sleep
##
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Topbar:
    def __init__(self, driver):
        self.driver = driver
        self.user_btn = self.driver.find_element(By.ID, "menuUserLink")
        self.wait10 = WebDriverWait( self.driver, 10)
        self.menu_options = self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>label")

    ## in-class methods:
    def wait_click_item_btn(self, item_btn):
        # self.wait10.until(EC.element_to_be_clickable(self.user_btn))
        self.user_btn.click()
        self.user_btn.send_keys(Keys.ESCAPE)
        print("clicked ESCAPE")
        # self.wait10.until(EC.element_to_be_clickable(item_btn))
        ## !!! this IS a sync problem. the wait doesn't work. the sleep does.
        sleep(3)
        item_btn.click()
    ##

    def click_menu_item(self, index: int):
        # self.user_btn.click()
        self.wait_click_item_btn(self.menu_options[index])

    def click_my_account(self):
        # my_account = self.driver.find_element(By.LINK_TEXT,"My account")
        # self.user_btn.click()
        # my_account = self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle>label[translate='My_account']")
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle>label[translate='My_account']"))
        # my_account.click()

    def click_my_orders(self):
        # self.user_btn.click()
        # my_orders = self.driver.find_element(By.LINK_TEXT, "My orders")
        # self.wait_click_item_btn(self.driver.find_element(By.LINK_TEXT, "My orders"))
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']"))
        # my_orders.click()

    def click_sign_out(self):
        self.user_btn.click()
        sign_out = self.driver.find_element(By.LINK_TEXT, "Sign out")
        self.wait_click_item_btn(sign_out)
        # sign_out.click()

    def click_cart(self):
        cart = self.driver.find_element(By.ID, "menuCart")
        cart.click()

    def click_aos_logo(self):
        aos_logo = self.driver.find_element(By.CSS_SELECTOR, "a[href='#/']")
        aos_logo.click()
