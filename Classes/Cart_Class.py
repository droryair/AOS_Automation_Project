from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
## IN-CLASS METHODS:
    1. get_list_cells_elems- receives an index, and returns a list including the column matching to the index.
    2. refresh_table- refresh self.table_rows in case something changed.
    
## GET METHODS:
    1. get_products_names- returns a list of all of the products' names in the cart.
    2. get_products_quantities- returns a list of all of the products' quantities in the cart.
    3. get_products_colors- returns a list of all of the products' colors in the cart.
    4. get_products_price- returns a list of all of the products' prices in the cart.
    
## CLICK METHODS:
    1. click_checkout- clicks the 'Checkout' button.
    2. click_edit- given an index clicks 'Edit' button of the product suiting that index.
    
## BOOLEAN METHODS:
    1. is_cart_empty- returns boolean value for the emptiness of the cart.
"""


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.table_rows = self.driver.find_elements(By.CSS_SELECTOR, "div[id=shoppingCart]>table>tbody>tr")
        self.wait10 = WebDriverWait(self.driver, 10)

    ##  IN-CLASS METHODS  ##

    # receives an index, and returns a list including the column matching to the index.
    def get_list_cells_elems(self, index: int):
        """
        :param index: an index matching a wanted column in the cart table.
                      (for example: 'quantities' column's index is 4)
        :return: a list including all of the cells' ELEMENTS from the column matching the index
        """
        # return map(lambda row: row.find_elements(By.TAG_NAME, 'td')[index], self.table_rows)
        self.refresh_table()
        lst = []
        for row in self.table_rows:
            row_cells = row.find_elements(By.TAG_NAME, 'td')
            lst.append(row_cells[index])
        return lst

    ## refresh self.table_rows in case something changed
    def refresh_table(self):
        """
        :functionality: refresh the cart in case something changed.
        :return:None
        """
        self.table_rows = self.driver.find_elements(By.CSS_SELECTOR, "div[id=shoppingCart]>table>tbody>tr")

    ##  ===

    ## GET METHODS: ##

    # returns a list of all of the products' names in the cart
    def get_products_names(self):
        """
        :return: a list of all of the products' names in the cart
                (index 0 = top product's name)
        """
        names_elems = self.get_list_cells_elems(1)
        names = []
        for name_elem in names_elems:
            names.append(name_elem.text)
        return names

    # returns a list of all of the products' quantities in the cart
    def get_products_quantities(self):
        """
        :return: a list of all of the products' quantities in the cart
                (index 0 = top product's quantity)
        """
        quantities_elems = self.get_list_cells_elems(4)
        quantities = []
        for quant_elem in quantities_elems:
            quantities.append(quant_elem.text)
            # quantities.append(self.str_to_num(quant_elem.text))
        return quantities

    # returns a list of all of the products' colors in the cart
    def get_products_colors(self):
        """
        :return: a list of all of the products' colors in the cart
                (index 0 = top product's color)
        """
        colors_tds = self.get_list_cells_elems(3)
        colors = []
        for color_td in colors_tds:
            colors.append(color_td.find_element(By.TAG_NAME, "span").get_attribute("title"))
        return colors

    # returns a list of all of the products' prices in the cart
    def get_products_price(self):
        """
        :return: a list of all of the products' prices in the cart
                (index 0 = top product's price)
        """
        prices_tds = self.get_list_cells_elems(5)
        prices = []
        for price_td in prices_tds:
            price_str = price_td.find_element(By.TAG_NAME, 'p').text
            prices.append(price_str)
            # prices.append(self.str_to_num(price_str))
        return prices

    ## CLICK METHODS ##

    # clicks the 'Checkout' button
    def click_checkout(self):
        """
        :functionality: clicks the 'Checkout' button
        :return: None
        """
        checkout_btn = self.driver.find_element(By.ID, "checkOutButton")
        checkout_btn.click()

    # given an index clicks 'Edit' button of the product suiting that index
    def click_edit(self, index):
        # ! add an 'how_many_products' to check if the given index is out of range? !
        """
        :param index: index of wanted product
        :functionality: clicks the 'Edit' button of the product suiting the given index
        :return: None
        """
        self.refresh_table()
        if not self.is_cart_empty():
            tds = self.table_rows[index].find_elements(By.TAG_NAME, "td")
            span = tds[len(tds)-1].find_element(By.TAG_NAME, "span")
            edit_btn = span.find_element(By.LINK_TEXT, "EDIT")
            self.wait10.until(EC.element_to_be_clickable((edit_btn)))
            edit_btn.click()

    ## BOOLEAN METHODS ##

    # returns boolean value for the emptiness of the cart
    def is_cart_empty(self):
        """
        :functionality: checks if the cart is empty or not.
        :return: True if empty, False if not empty.
        """
        return self.driver.find_element(By.CSS_SELECTOR, "#shoppingCart>div>label[translate='Your_shopping_cart_is_empty']").is_displayed()


