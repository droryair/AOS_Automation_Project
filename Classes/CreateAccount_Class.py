"""'
create account (username, email password, confirm password, i agree checkbox, register btn)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver
        self.wait10 = WebDriverWait(self.driver,10)

    ## in-class functions:
    def wait_for_register_btn(self,btn):
        try:
            self.wait10.until(EC.element_to_be_clickable(btn))
            btn.click()
        except:
            print("Register button is not clickable yet. trying again...")
            self.check_i_agree()
            self.click_register()
    ##


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
        i_agree_checkbox = self.driver.find_element(By.CSS_SELECTOR, "#formCover>sec-view>div>label")
        i_agree_checkbox.click()

    def click_register(self):
        register_btn = self.driver.find_element(By.ID, "register_btnundefined")
        self.wait_for_register_btn(register_btn)
