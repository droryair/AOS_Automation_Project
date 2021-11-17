

from selenium.webdriver.common.by import By
 #  div[id=myAccountContainer]>div>table>tbody>tr>td:nth-child(1)>label

class MyOrders:
    def __init__(self, driver):
        self.driver = driver
        self.table_rows = self.driver.find_elements(By.XPATH,"//div[@id='myAccountContainer']/div/table/tbody/tr[@class='ng-scope']")

    ## in-class methods:

    #refresh orders table
    def refresh_table(self):
        self.table_rows = self.driver.find_elements(By.XPATH,"//div[@id='myAccountContainer']/div/table/tbody/tr[@class='ng-scope']")

    ##


    def get_orders_numbers(self):
        order_numbers_elements = self.driver.find_elements(By.XPATH, "//div[@id='myAccountContainer']/div/table/tbody/tr/td[1]/label")
        print("len(order_numbers_elements)", len(order_numbers_elements))
        orders_numbers = []
        for element in order_numbers_elements:
            orders_numbers.append(element.text)
        print("len(orders_numbers)", len(orders_numbers))
        print(orders_numbers[0])
        return orders_numbers

    def get_total_orders_costs(self):
        # tr[class ="ng-scope"]>td[last]>label.text
        self.refresh_table()

        total_orders = []
        for row in self.table_rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            td = tds[len(tds)-1].find_element(By.TAG_NAME, "label")
            total_orders.append(td.text)
        print("MyOrders->28->total_orders: ", total_orders)
        return total_orders
