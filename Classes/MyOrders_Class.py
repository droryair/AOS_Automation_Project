

from selenium.webdriver.common.by import By
 #  div[id=myAccountContainer]>div>table>tbody>tr>td:nth-child(1)>label

class MyOrders:
    def __init__(self, driver):
        self.driver = driver

    def get_orders_numbers(self):
        order_numbers_elements = self.driver.find_elements(By.XPATH, "//div[@id='myAccountContainer']/div/table/tbody/tr/td[1]/label")
        print("len(order_numbers_elements)", len(order_numbers_elements))
        orders_numbers = []
        for element in order_numbers_elements:
            orders_numbers.append(element.text)
        print("len(orders_numbers)", len(orders_numbers))
        print(orders_numbers[0])
        return orders_numbers

