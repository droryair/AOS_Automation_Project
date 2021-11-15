"""
!!! exists both before registration and after ordering !!!

order payment (next)
"""

from selenium.webdriver.common.by import By

class OrderPayment:
    def __init__(self, driver):
        self.driver = driver

    def click_registration(self):
        registration_btn = self.driver.find_element(By.ID,"registration_btnundefined")
        registration_btn.click()


