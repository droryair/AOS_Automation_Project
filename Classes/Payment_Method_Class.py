"""
payment method (SafePay, username, password, Pay Now btn,)
                (MasterCredit, Card number, cvv number,mm,yyyy, cardholder name)
"""
from selenium.webdriver.common.by import By


class PaymentMethod:
    def __init__(self, driver):
        self.driver = driver