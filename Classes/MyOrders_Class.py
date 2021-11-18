from selenium.webdriver.common.by import By
"""
## IN-CLASS METHODS:
    1.refresh_table- refresh orders table in case something changed.
## GET METHODS:
    1. get_orders_numbers- returns a list containing all of the user's orders numbers, as strings.
    2. get_total_orders_costs- returns a list of all of the user's orders' total price, as a string.
"""

class MyOrders:
    def __init__(self, driver):
        self.driver = driver
        self.table_rows = self.driver.find_elements(By.XPATH,"//div[@id='myAccountContainer']/div/table/tbody/tr[@class='ng-scope']")

    ## IN-CLASS METHODS

    # refresh orders table in case something changed
    def refresh_table(self):
        """
        :functionality: refresh orders table in case something changed.
        :return: None
        """
        self.table_rows = self.driver.find_elements(By.XPATH, "//div[@id='myAccountContainer']/div/table/tbody/tr[@class='ng-scope']")

    ## ===

    ## GET METHODS

    # returns a list containing all of the user's orders numbers, as strings.
    def get_orders_numbers(self):
        """
        :return: a list containing all of the user's orders numbers, as strings.
        """
        self.refresh_table()
        order_numbers_elements = []
        for row in self.table_rows:
            tds = row.find_elements(By.TAG_NAME, 'td')  # columns
            td = tds[0]  # 'order number' column
            order_numbers_elements.append(td.find_element(By.TAG_NAME, 'label'))
        orders_numbers = []
        for element in order_numbers_elements:
            orders_numbers.append(element.text)
        print("order numbers:", orders_numbers)
        return orders_numbers

    # returns a list of all of the user's orders' total price, as a string.
    def get_total_orders_costs(self):
        """
        :return: returns a list of all of the user's orders' total price, as a string.
        """
        self.refresh_table()
        total_orders = []
        for row in self.table_rows:
            tds = row.find_elements(By.TAG_NAME, "td")  # columns
            td = tds[len(tds)-1].find_element(By.TAG_NAME, "label")  # 'total price' column
            total_orders.append(td.text)
        return total_orders
