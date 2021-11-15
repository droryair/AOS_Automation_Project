"""'
create account (username, email password, confirm password, i agree checkbox, register btn)
"""
from selenium.webdriver.common.by import By


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_input = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username_input.send_keys(username)

    def set_password(self, password, confirm=False):
        password_input = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password_input.send_keys(password)
        if confirm:
            # set password both to password and confirm password
            confirm_pass_input = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
            confirm_pass_input.send_keys(password)

    def set_confirm_password(self, password):
        confirm_pass_input = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        confirm_pass_input.send_keys(password)

    def set_email(self, email):
        email_input = self.driver.find_element(By.NAME, "emailRegisterPage")
        email_input.send_keys(email)

    def check_i_agree(self):
        i_agree_checkbox = self.driver.find_element(By.NAME, "i_agree")
        i_agree_checkbox.click()

    def click_register(self):
        register_btn = self.driver.find_element(By.ID, "register_btnundefined")
        register_btn.click()