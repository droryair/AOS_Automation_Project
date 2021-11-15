"""
cart (quantity, name, color, price, remove, "shopping cart" text, Total)
"""
from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.table_rows = self.driver.find_elements(By.CSS_SELECTOR,"div[id=shoppingCart]>table>tbody>tr")

## == inner-class functions == ##

    # this function will receive a string and turn it into a number (int/float)
    # !!! move to the main file? what if we want the string and not the number itself? !!! #
    '''    
    def str_to_num(self, stri: str):
        """
        :param stri: string including numeric characters and no more than one dot (.)
        :return: that string as a number type (int/float), depends on the existence of a dot (.)
        """
        is_float = False
        for char in stri:
            if not char.isnumeric():
                if char == '.':
                    is_float = True
                    continue
                stri = stri.replace(char, '')
        if is_float:
            return float(stri)
        return int(stri)
    '''

    # this function will receive an index, and will return a list including the column matching to the index.
    def get_list_cells_elems(self, index: int):
        """
        :param index: an index matching a wanted column in the cart table.
                      (for example: 'quantities' column's index is 4)
        :return: a list including all of the cells' ELEMENTS from the column matching the index
        """
        lst = []
        for row in self.table_rows:
            row_cells = row.find_elements(By.TAG_NAME, 'td')
            lst.append(row_cells[index])
        return lst

##  ===

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


