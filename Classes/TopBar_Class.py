from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
"""
## IN-CLASS METHODS:
    1. wait_click_item_btn- receives a button element corresponding with one of the user's menu and clicks it if any user is logged in
    2. show_cart_popup- hovers over the 'cart' icon to show it's popup.
## GET METHODS:
    1. get_username- returns the current logged-in username, or None if not logged in
    2. get_total_items- returns the total items from the cart icon
    3. is_logged_in- returns boolean value for weather anyone is logged in or not
## CLICK METHODS:
    1. click_aos_logo- clicks the aos logo to go to the 'home' page
    2. click_cart-  clicks the 'cart' icon to go to the cart page.
## USER ICON MENU METHODS:
    1. login- receives username and password strings , enters them to the corresponding input fields and clicks the 'login' button
    2. click_my_account- clicks 'my account' button
    3. click_my_orders- clicks 'my orders' button
    4. click_sign_out- clicks 'sign out' button
## POP-UP CART METHODS:
    1. get_items_from_popup_cart- returns a list of items' details in the popup cart as a dictionary.
    2. get_items_elems_from_popup_cart- returns a list of the items' elements in the pop-up cart
    3. remove_item_from_popup_cart- receives an item's index (int), removes it from the cart and returns the removed item.
## LOCATION IN THE SITE METHODS:
    1. get_page- returns the name of the current page (str)
    2. go_back- goes back to the previous page
## USER DELETING METHODS:
    1. delete_logged_user- goes to the current logged in user, and deletes their account
"""


class Topbar:
    def __init__(self, driver):
        self.driver = driver
        self.user_btn = self.driver.find_element(By.ID, "menuUserLink")
        self.wait10 = WebDriverWait(self.driver, 10)
        self.wait3 = WebDriverWait(self.driver, 3)
        self.menu_options = self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>label")

    ## IN-CLASS METHODS

    # receives a button element corresponding with one of the user's menu and clicks it if any user is logged in
    def wait_click_item_btn(self, item_btn):
        """
        :param item_btn: a button element corresponding with one of the user's menu
        :functionality: clicks the given button if any user is logged in
        :return: None
        """
        if self.is_logged_in():
            self.user_btn.click()
            self.user_btn.send_keys(Keys.ESCAPE)  # in case the cart popup is visible
            self.wait10.until(EC.element_to_be_clickable((item_btn)))
            item_btn.click()
        else:
            print("No user is logged in. Please log in first.")

    # hovers over the 'cart' icon to show it's popup
    def show_cart_popup(self):
        """
        :functionality: hovers over the 'cart' icon to show it's popup
        :return: None
        """
        cart_icon = self.driver.find_element(By.ID, "menuCart")
        ActionChains(self.driver).move_to_element(cart_icon).perform()
        self.wait3.until(EC.visibility_of((self.driver.find_element(By.CSS_SELECTOR, '#toolTipCart>div>table'))))

    ##

    ## GET METHODS

    # returns the current logged-in username, or None if not logged in
    def get_username(self):
        """
        :return: the current logged-in username, or None if not logged in.
        """
        if self.is_logged_in():
            username = self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span').text
            return username
        print("no user is logged in")
        return

    # returns the total items from the cart icon
    def get_total_items(self):
        """
        :return: the total items from the cart icon
        """
        amount_str = self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink>span").text
        if amount_str == '':
            return 0
        return int(amount_str)

    # returns boolean value for weather anyone is logged in or not
    def is_logged_in(self):
        """
        :return: a boolean value for weather anyone is logged in or not
        """
        self.wait3.until(EC.element_to_be_clickable(self.user_btn))
        username = self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span').text
        if len(username) > 0:
            return True
        return False

    ## CLICK METHODS

    # clicks the aos logo to go to the 'home' page
    def click_aos_logo(self):
        """
        :functionality: clicks the aos logo to go to the 'home' page
        :return: None
        """
        aos_logo = self.driver.find_element(By.CSS_SELECTOR, "a[href='#/']")
        self.wait10.until(EC.element_to_be_clickable(aos_logo))
        aos_logo.click()

    # clicks the 'cart' icon to go to the cart page.
    def click_cart(self):
        """
        :functionality: clicks the 'cart' icon to go to the cart page.
        :return: None
        """
        cart = self.driver.find_element(By.ID, "menuCart")
        cart.click()
        ActionChains(self.driver).move_to_element(self.user_btn).perform()
        self.user_btn.send_keys(Keys.ESCAPE)
        # waiting for cat popup to close
        self.wait10.until(EC.invisibility_of_element(((self.driver.find_element(By.CSS_SELECTOR, '#toolTipCart>div>table')))))

    ## USER ICON MENU METHODS

    # receives username and password strings , enters them to the corresponding input fields and clicks the 'login' button
    def login(self, username: str, password: str):
        """
        :param username: username string
        :param password: password string
        :functionality: enters the username and the password to the corresponding input fields and clicks the 'login' button
        :return: None
        """
        if not self.is_logged_in():
            self.user_btn.click()
            username_input = self.driver.find_element(By.NAME, "username")
            password_input = self.driver.find_element(By.NAME, "password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            self.wait3.until(EC.element_to_be_clickable((self.driver.find_element(By.ID, "sign_in_btnundefined"))))
            sign_in_btn = self.driver.find_element(By.ID, "sign_in_btnundefined")
            sign_in_btn.click()
            message = self.driver.find_element(By.ID, "signInResultMessage").text
            if not self.is_logged_in() and message == 'Incorrect user name or password.':
                print("Incorrect username or password. Please try again.")
            else:
                self.wait3.until(EC.visibility_of((self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span'))))
        else:
            print("A user is already signed in")

    # clicks 'my account' button
    def click_my_account(self):
        """
        :functionality: clicks 'my account' button
        :return: None
        """
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle>label[translate='My_account']"))

    # clicks 'my orders' button
    def click_my_orders(self):
        """
        :functionality: clicks 'my account' button
        :return: None
        """
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']"))

    # clicks 'sign out' button
    def click_sign_out(self):
        """
        :functionality: clicks 'sign out' button if a user is logged in
        :return: None
        """
        if self.is_logged_in():
            username_elem = self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span')
            self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][role='link']"))
            self.wait3.until(EC.invisibility_of_element((username_elem)))
        else:
            print('no one was logged in.')

    ## POP-UP CART METHODS

    # returns a list of items' details in the popup cart as a dictionary.
    def get_items_from_popup_cart(self):
        """
        :return: a list of items' details in the popup cart as a dictionary
        """
        if self.get_total_items() > 0:
            self.show_cart_popup()
            items = []
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
            for row in rows:
                cart_items = row.find_elements(By.XPATH, ".//td[2]/a")
                for cart_item in cart_items:
                    name = cart_item.find_element(By.TAG_NAME, 'h3').text
                    quant = cart_item.find_element(By.XPATH, './/label[1]').text
                    color = cart_item.find_element(By.XPATH, './/label[2]/span').text
                    items.append({'name': name, 'quantity': quant, 'color': color})
            items.reverse()
            return items
        else:
            print("The cart is empty")
            return []

    # returns a list of the items' elements in the pop-up cart
    def get_items_elems_from_popup_cart(self):
        """
        :return: a list of the items' elements in the pop-up cart
        """
        if self.get_total_items() > 0:
            self.show_cart_popup()
            items_elems = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
            items_elems.reverse()
            return items_elems
        else:
            print("The cart is empty")
            return []

    # receives an item's index (int), removes it from the cart and returns the removed item.
    def remove_item_from_popup_cart(self, item_index: int):
        self.show_cart_popup()
        items = self.get_items_elems_from_popup_cart()
        removed_item = items[item_index]
        remove_btn = items[item_index].find_element(By.CSS_SELECTOR, ".closeDiv>div")
        remove_btn.click()
        return removed_item

    ## LOCATION IN THE SITE METHODS

    # returns the name of the current page (str)
    def get_page(self):
        """
        :return:  the name of the current page (str)
        """
        path = self.driver.find_elements(By.CSS_SELECTOR, "nav>a")
        if len(path) == 0:
            return "Home"
        else:
            return path[len(path)-1].text

    # goes back to the previous page
    def go_back(self):
        """
        :functionality: goes back to the previous page
        :return: None
        """
        self.driver.back()

    ## USER DELETING METHODS

    # goes to the current logged in user, and deletes their account
    def delete_logged_user(self):
        """
        :functionality: goes to the current- logged in user, and deletes their account
        :return: None
        """
        self.click_my_account()
        delete_account_btn = self.driver.find_element(By.CSS_SELECTOR, "div.deleteBtnText")
        delete_account_btn.click()
        # waiting until the confirmation pop-up will appear. if it doesn't- clicking on 'delete account' button again.
        try:
            self.wait3.until(EC.visibility_of((self.driver.find_element(By.CSS_SELECTOR, "div[id='deleteAccountPopup']>div[class='deleteBtnContainer']>div[class='deletePopupBtn deleteRed']"))))
        except:
            delete_account_btn.click()
        self.driver.find_element(By.CSS_SELECTOR, "div[id='deleteAccountPopup']>div[class='deleteBtnContainer']>div[class='deletePopupBtn deleteRed']").click()
