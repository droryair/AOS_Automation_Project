"""
!!! exists both before registration and after ordering !!!

order payment (next)
"""

from selenium.webdriver.common.by import By

class OrderPayment:
    def __init__(self, driver):
        self.driver = driver