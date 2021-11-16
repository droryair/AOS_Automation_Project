"""
!!! exists both before registration and after ordering !!!

order payment (next)
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderPayment:
    def __init__(self, driver):
        self.driver = driver
        self.wait3 = WebDriverWait(self.driver, 3)
    ## in-class functions

    def wait_for_pay_now_btn(self, btn):
        try:
            self.wait3.until(EC.element_to_be_clickable(btn))
            btn.click()
        except:
            print("Can't click the 'order now' button")

    ##

    def click_registration(self):
        registration_btn = self.driver.find_element(By.ID, "registration_btnundefined")
        registration_btn.click()

## available only if a user is logged in:

    def click_next(self):
        next_btn = self.driver.find_element(By.ID, "next_btn")
        next_btn.click()

    def set_safepay_username(self, username):
        # input[name='safepay_username']
        username_input = self.driver.find_element(By.NAME, "safepay_username")
        username_input.send_keys(username)

    def set_safepay_password(self, password):
        # input[name='safepay_password']
        password_input = self.driver.find_element(By.NAME, "safepay_password")
        password_input.send_keys(password)

    def click_pay_now(self):
        # pay_now_btn_SAFEPAY
        pay_now_btn = self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")
        self.wait_for_pay_now_btn(pay_now_btn)

    def get_order_number(self):
        return self.driver.find_element(By.ID, "orderNumberLabel").text
