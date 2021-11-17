"""
top bar (user, cart)
top bar- login/logout
top bar- path bar
top bar- floating cart

"""
## delete
from time import sleep
##
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Topbar:
    def __init__(self, driver):
        self.driver = driver
        self.user_btn = self.driver.find_element(By.ID, "menuUserLink")
        self.wait10 = WebDriverWait(self.driver, 10)
        self.wait3 = WebDriverWait(self.driver, 3)
        self.menu_options = self.driver.find_elements(By.CSS_SELECTOR, "#loginMiniTitle>label")

    ## in-class methods:
    #
    # def click_user_icon(self):
    #     self.user_btn.click()
    #     popup = self.driver.find_element(By.CLASS_NAME,"PopUp")
    #     if popup.is_displayed():
    #

    def wait_click_item_btn(self, item_btn):
        # self.wait10.until(EC.element_to_be_clickable(self.user_btn))
        if self.is_logged_in():
            # self.wait3.until(EC.element_to_be_clickable(((self.user_btn))))
            self.user_btn.click()
            self.user_btn.send_keys(Keys.ESCAPE)  # in case the cart popup is visible
            self.wait10.until(EC.element_to_be_clickable((item_btn)))
            item_btn.click()
        else:
            print("No user is logged in. Please log in first.")

    def is_logged_in(self):
        # #menuUserLink>span
        self.wait3.until(EC.element_to_be_clickable(self.user_btn))
        username = self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span').text
        if len(username) > 0:
            return True
        return False

    def show_cart_popup(self):
        cart_icon = self.driver.find_element(By.ID, "menuCart")
        ActionChains(self.driver).move_to_element(cart_icon).perform()
        self.wait3.until(EC.visibility_of((self.driver.find_element(By.CSS_SELECTOR, '#toolTipCart>div>table'))))

    # def is_cart_empty(self):
    #     self.get_total_items()


    ##

    def click_menu_item(self, index: int):
        # self.user_btn.click()
        self.wait_click_item_btn(self.menu_options[index])

    def click_my_account(self):
        # my_account = self.driver.find_element(By.LINK_TEXT,"My account")
        # self.user_btn.click()
        # my_account = self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle>label[translate='My_account']")
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "#loginMiniTitle>label[translate='My_account']"))
        # my_account.click()

    def click_my_orders(self):
        # self.user_btn.click()
        # my_orders = self.driver.find_element(By.LINK_TEXT, "My orders")
        # self.wait_click_item_btn(self.driver.find_element(By.LINK_TEXT, "My orders"))
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][role='link']"))
        # my_orders.click()

    def login(self, username, password):
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
            print("A user is already signed in")

    def click_sign_out(self):
        # sign_out = self.driver.find_element(By.LINK_TEXT, "Sign out")
        # self.wait_click_item_btn(sign_out)
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][role='link']"))
        # sign_out.click()

    def click_aos_logo(self):
        aos_logo = self.driver.find_element(By.CSS_SELECTOR, "a[href='#/']")
        aos_logo.click()

    def click_cart(self):
        cart = self.driver.find_element(By.ID, "menuCart")
        cart.click()

    def get_total_items(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink>span").text

    def get_items_from_popup_cart(self):
        if self.get_total_items() != '':
            # toolTipCart>div>table>tbody>tr
            self.show_cart_popup()
            items_names = []
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
            for row in rows:
                details = row.find_elements(By.CSS_SELECTOR, "td:nth-child(2)>a")
                items_names.append(details[0].text)
            for i in range(len(items_names)):
                name = items_names.pop().split("QTY:")[0].rstrip("\n")
                items_names.append(name)
            return items_names
        else:
            print("The cart is empty")
            return []

    def remove_item_from_popup_cart(self, item_index):
        # .closeDiv
        self.show_cart_popup()
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
        remove_btn = rows[item_index].find_element(By.CSS_SELECTOR, ".closeDiv>div")
        remove_btn.click()

