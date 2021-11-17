"""
!!! exists both before registration and after ordering !!!

order payment (next)
"""
from random import randint

from selenium.webdriver import Keys
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
            print("Can't click the 'pay now' button")

    # in case a creditcard details are already registered and we want deit them
    def edit_paymet_details(self):
        edit_btn = self.driver.find_element(By.CSS_SELECTOR, "label[translate=Edit]")
        # edit_btn = self.driver.find_element(By.LINK_TEXT, "Edit")
        edit_btn.click()

    def try_editing(self, element):
        try:
            self.wait3.until(EC.visibility_of(element))
        except:
            self.edit_paymet_details()



    ##

    def click_registration(self):
        registration_btn = self.driver.find_element(By.ID, "registration_btnundefined")
        registration_btn.click()


    ## LOGIN ##
    def set_username(self, username):
        username_input = self.driver.find_element(By.NAME, "usernameInOrderPayment")
        self.try_editing(username_input)
        username_input.send_keys(username)

    def set_password(self, password):
        password_input = self.driver.find_element(By.NAME, "passwordInOrderPayment")
        self.try_editing(password_input)
        password_input.send_keys(password)

    def click_login(self):
        login_btn = self.driver.find_element(By.ID, "login_btnundefined")
        self.wait3.until(EC.element_to_be_clickable(login_btn))
        login_btn.click()

## available only if a user is logged in:

    def click_next(self):
        next_btn = self.driver.find_element(By.ID, "next_btn")
        next_btn.click()

    ## SAFEPAY   ##

    def set_safepay_username(self, username):
        # input[name='safepay_username']
        username_input = self.driver.find_element(By.NAME, "safepay_username")
        self.try_editing(username_input)
        username_input.send_keys(username)

    def set_safepay_password(self, password):
        # input[name='safepay_password']
        password_input = self.driver.find_element(By.NAME, "safepay_password")
        self.try_editing(password_input)
        password_input.send_keys(password)

    ## MASTERCARD ##
    def select_mastercard(self):
        # input[name='masterCredit']
        radio = self.driver.find_element(By.NAME, "masterCredit")
        radio.click()

    def set_mastercard_card_number(self, card_number):
        card_number_input = self.driver.find_element(By.NAME, "card_number")
        self.try_editing(card_number)
        card_number_input.clear()
        card_number_input.send_keys(card_number)
        # self.wait3.until(EC.text_to_be_present_in_element_attribute((card_number_input), 'value', card_number))
        try:
            self.wait3.until(EC.text_to_be_present_in_element_value((By.NAME, "card_number"), card_number))
        except:
            pass

    def set_mastercard_cvv_number(self, cvv_number):
        cvv_number_input = self.driver.find_element(By.NAME, "cvv_number")
        self.try_editing(cvv_number_input)
        cvv_number_input.clear()
        # cvv_number_input.send_keys(0)
        cvv_number_input.send_keys(cvv_number)
        try:
            self.wait3.until(EC.text_to_be_present_in_element_value((By.NAME, "cvv_number"), cvv_number))
        except:
            pass

    def set_mastercard_cardholder_name(self, cardholder_name):
        cardholder_name_input = self.driver.find_element(By.NAME, "cardholder_name")
        self.try_editing(cardholder_name_input)
        cardholder_name_input.clear()
        cardholder_name_input.send_keys(cardholder_name)
        try:
            self.wait3.until(EC.text_to_be_present_in_element_value((By.NAME, "cardholder_name"), cardholder_name))
        except:
            pass

    def click_pay_now_mastercard(self):
        # pay_now_btn_MasterCredit
        pay_now_btn = self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")
        self.wait_for_pay_now_btn(pay_now_btn)

    def click_pay_now_safepay(self):
        # pay_now_btn_SAFEPAY
        pay_now_btn = self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")
        self.wait_for_pay_now_btn(pay_now_btn)

    def get_order_number(self):
        self.wait3.until(EC.visibility_of(self.driver.find_element(By.ID, "orderNumberLabel")))
        return self.driver.find_element(By.ID, "orderNumberLabel").text
