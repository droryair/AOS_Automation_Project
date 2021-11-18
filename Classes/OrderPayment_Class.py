from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
## IN-CLASS METHODS:
    1. wait_for_pay_now_btn- waiting for 'pay now' button to be clickable
    2. try_editing- waits to see if mastercard details are editable. if not- clicks the 'edit' button
    3. click_edit_paymet_details- clicking on 'Edit' button for editing 'Mastercard' information
## SET METHODS -> LOGIN:
    1. set_username- receives a username string and enters it to the corresponding input field
    2. set_password- receives a password string and enters it to the corresponding input field
## CLICK METHODS:
    1. click_registration- clicks the 'registration' button (appears after clicking 'checkout')
    2. click_login- clicks the 'login' button (appears after clicking 'checkout')
    3. click_next- clicks 'next' to move to the 'payment details'
## SAFEPAY:
    1. set_safepay_username- receives a 'safepay' username string and enters it to the corresponding input field
    2. set_safepay_password- receives a 'safepay' password string and enters it to the corresponding input field
## MASTERCARD:
    1. select_mastercard- clicks the 'mastercard' radio button
    2. set_mastercard_card_number- receives a 'mastercard' card number int and enters it to the corresponding input field
    3. set_mastercard_cvv_number- receives a cvv number int and enters it to the corresponding input field
    4. set_mastercard_cardholder_name- receives a cardholder name string and enters it to the corresponding input field
    5. click_pay_now_mastercard- clicks the 'pay now' button for 'mastercard' payment method
    6. click_pay_now_safepay- clicks the 'pay now' button for 'safepay' payment method
## SUCCESSFUL ORDERING:
    1. get_order_number- returns the order's number as string after committing it successfully.
    
"""


class OrderPayment:
    def __init__(self, driver):
        self.driver = driver
        self.wait3 = WebDriverWait(self.driver, 3)

    ## IN-CLASS METHODS

    # waiting for 'pay now' button to be clickable
    def wait_for_pay_now_btn(self, btn):
        """
        :param btn: a 'pay now' button element
        :return: None
        """
        try:
            self.wait3.until(EC.element_to_be_clickable(btn))
            btn.click()
        except:
            print("Can't click the 'pay now' button")

    # in case the mastercard details are already registered and we want edit them

    # waits to see if mastercard details are editable. if not- clicks the 'edit' button
    def try_editing(self, element):
        """
        :param element: an input- type element
        :functionality: waiting for element to be editable. if not- clicking on 'Edit' button.
        :return: None
        """
        try:
            self.wait3.until(EC.visibility_of(element))
        except:
            self.click_edit_paymet_details()

    # clicking on 'Edit' button for editing 'Mastercard' information
    def click_edit_paymet_details(self):
        """
        "functionality: clicking on 'Edit' button for editing 'Mastercard' information
        :return:
        """
        edit_btn = self.driver.find_element(By.CSS_SELECTOR, "label[translate=Edit]")
        edit_btn.click()

    ##

    ## SET METHODS -> LOGIN

    # receives a username string and enters it to the corresponding input field
    def set_username(self, username: str):
        """
        :param username: username string
        :functionality: enters the username to the corresponding input field
        :return: None
        """
        username_input = self.driver.find_element(By.NAME, "usernameInOrderPayment")
        self.try_editing(username_input)
        username_input.send_keys(username)

    # receives a password string and enters it to the corresponding input field
    def set_password(self, password: str):
        """
        :param password: password string
        :functionality: enters the password to the corresponding input field
        :return: None
        """
        password_input = self.driver.find_element(By.NAME, "passwordInOrderPayment")
        self.try_editing(password_input)
        password_input.send_keys(password)

    ## CLICK METHODS

    # clicks the 'registration' button (appears after clicking 'checkout')
    def click_registration(self):
        """
        :functionality: clicks the 'registration' button
        :return: None
        """
        registration_btn = self.driver.find_element(By.ID, "registration_btnundefined")
        registration_btn.click()

    # clicks the 'login' button (appears after clicking 'checkout')
    def click_login(self):
        """
        :functionality: clicks the 'login' button.
        :return: None
        """
        login_btn = self.driver.find_element(By.ID, "login_btnundefined")
        self.wait3.until(EC.element_to_be_clickable(login_btn))
        login_btn.click()

    # clicks 'next' to move to the 'payment details'
    def click_next(self):
        """
        :functionality: clicks' next' to move to the 'payment details'
        :return: None
        """
        next_btn = self.driver.find_element(By.ID, "next_btn")
        next_btn.click()

    ## SAFEPAY

    # receives a 'safepay' username string and enters it to the corresponding input field
    def set_safepay_username(self, username: str):
        """
        :param username: username string
        :functionality: enters the username to the corresponding input field
        :return: None
        """
        username_input = self.driver.find_element(By.NAME, "safepay_username")
        self.try_editing(username_input)
        username_input.send_keys(username)

    # receives a 'safepay' password string and enters it to the corresponding input field
    def set_safepay_password(self, password: str):
        """
        :param password: password string
        :functionality:enters the password to the corresponding input field
        :return: None
        """
        password_input = self.driver.find_element(By.NAME, "safepay_password")
        self.try_editing(password_input)
        password_input.send_keys(password)

    ## MASTERCARD ##

    # clicks the 'mastercard' radio button
    def select_mastercard(self):
        """
        :functionality: clicks the 'mastercard' radio button
        :return: None
        """
        radio = self.driver.find_element(By.NAME, "masterCredit")
        radio.click()

    # receives a 'mastercard' card number int and enters it to the corresponding input field
    def set_mastercard_card_number(self, card_number: int):
        """
        :param card_number: card number int
        :functionality: enters the card number to the corresponding input field
        :return: None
        """
        card_number_input = self.driver.find_element(By.NAME, "card_number")
        self.try_editing(card_number)
        card_number_input.clear()
        card_number_input.send_keys(card_number)
        card_number_input.send_keys(card_number)

    # receives a cvv number int and enters it to the corresponding input field
    def set_mastercard_cvv_number(self, cvv_number: int):
        """
        :param cvv_number: int
        :functionality: enters the cvv number to the corresponding input field
        :return: None
        """
        cvv_number_input = self.driver.find_element(By.NAME, "cvv_number")
        self.try_editing(cvv_number_input)
        cvv_number_input.clear()
        cvv_number_input.send_keys(cvv_number)

    # receives a cardholder name string and enters it to the corresponding input field
    def set_mastercard_cardholder_name(self, cardholder_name: str):
        """
        :param cardholder_name: cardholder name string
        :functionality: enters the cardholder name to the corresponding input field
        :return: None
        """
        cardholder_name_input = self.driver.find_element(By.NAME, "cardholder_name")
        self.try_editing(cardholder_name_input)
        cardholder_name_input.clear()
        cardholder_name_input.send_keys(cardholder_name)

    # clicks the 'pay now' button for 'mastercard' payment method
    def click_pay_now_mastercard(self):
        """
        :functionality: clicks the 'pay now' button for 'mastercard' payment method
        :return: None
        """
        pay_now_btn = self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")
        self.wait_for_pay_now_btn(pay_now_btn)

    # clicks the 'pay now' button for 'safepay' payment method
    def click_pay_now_safepay(self):
        """
        :functionality: clicks the 'pay now' button for 'safepay' payment method.
        :return: None
        """
        pay_now_btn = self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")
        self.wait_for_pay_now_btn(pay_now_btn)

    ## SUCCESSFUL ORDERING

    # returns the order's number as string after committing it successfully
    def get_order_number(self):
        """
        :functionality: gets the order number for the just-placed order.
        :return: order number as string.
        """
        self.wait3.until(EC.visibility_of(self.driver.find_element(By.ID, "orderNumberLabel")))
        return self.driver.find_element(By.ID, "orderNumberLabel").text
