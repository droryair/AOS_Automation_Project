"""'
create account (username, email password, confirm password, i agree checkbox, register btn)
"""
from selenium.webdriver.common.by import By


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver