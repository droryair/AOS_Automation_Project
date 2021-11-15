"""
!!! exists both before registration and after ordering !!!

order payment (next)
"""

from selenium.webdriver.common.by import By

class OrderPayment:
    def __init__(self, driver):
        self.driver = driver

    def click_registration(self):
        registration_btn = self.driver.find_element(By.ID, "registration_btnundefined")
        registration_btn.click()

## available only if a user is logged in:

    def click_next(self):
        next_btn = self.driver.find_element(By.ID, "next_btn")
        next_btn.click()
