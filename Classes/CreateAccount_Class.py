from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
## IN-CLASS METHODS:
    1. wait_for_register_btn- waiting for the ability to click the 'REGISTER' button.
## SET METHODS:
    1.set_username- fill the 'username' text field.
    2.set_password- fill the 'password' text field.
    3.set_confirm_password- fill the 'confirm password' text field.
    4.set_email- fill the 'email' text field.
## CLICK METHODS:
    1.check_i_agree- checks the required 'I agree' checkbox.
    2.click_register- clicks the 'REGISTER' button.
"""


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver
        self.wait10 = WebDriverWait(self.driver, 10)

    ## IN-CLASS METHODS
    # waiting for the ability to click the 'REGISTER' button
    def wait_for_register_btn(self, btn):
        """
        :param btn the 'REGISTER' button:
        :functionality: waiting for the ability to click the 'REGISTER' button.
        :return: None
        """
        try:
            self.wait10.until(EC.element_to_be_clickable(btn))
            btn.click()
        except:
            print("Register button is not clickable yet. trying again...")
            self.check_i_agree()
            self.click_register()
    ## ===

    ## SET METHODS

    # fill the 'username' text field
    def set_username(self, username):
        """
        :param username: input for the 'username' field
        :functionality: fill the 'username' text field
        :return: None
        """
        username_input = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username_input.send_keys(username)

    # fill the 'password' text field
    def set_password(self, password, confirm=False):
        """
        :param password: input for the 'password' field
        :param confirm: boolean for filling the 'confim password' input with the same value of 'password'
        :functionality: fill the 'password' text field
        :return: None
        """
        password_input = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password_input.send_keys(password)
        if confirm:
            # set password both to 'password' and 'confirm password'
            confirm_pass_input = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
            confirm_pass_input.send_keys(password)

    # fill the 'confirm password' text field
    def set_confirm_password(self, password):
        """
        :param password: input for the 'confirm password' field
        :functionality: fill the 'confirm password' text field
        :return: None
        """
        confirm_pass_input = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        confirm_pass_input.send_keys(password)

    # fill the 'email' text field
    def set_email(self, email):
        """
        :param email: input for the 'email' field
        :functionality: fill the 'email' text field
        :return: None
        """
        email_input = self.driver.find_element(By.NAME, "emailRegisterPage")
        email_input.send_keys(email)

    ## CLICK METHODS

    # checks the required 'I agree' checkbox.
    def check_i_agree(self):
        """
        :functionality: checks the required 'I agree' checkbox.
        :return: None
        """
        i_agree_checkbox = self.driver.find_element(By.CSS_SELECTOR, "#formCover>sec-view>div>label")
        i_agree_checkbox.click()

    # clicks the 'REGISTER' button.
    def click_register(self):
        """
        :functionality: clicks the 'REGISTER' button
        :return: None
        """
        register_btn = self.driver.find_element(By.ID, "register_btnundefined")
        self.wait_for_register_btn(register_btn)
