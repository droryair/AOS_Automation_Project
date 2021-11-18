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

    def get_username(self):
        if self.is_logged_in():
            username = self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span').text
            return username
        print("no user is logged in")
        return

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
                self.wait3.until(EC.visibility_of((self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span'))))
        else:
            print("A user is already signed in")

    def click_sign_out(self):
        # sign_out = self.driver.find_element(By.LINK_TEXT, "Sign out")
        # self.wait_click_item_btn(sign_out)
        username_elem = self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>span')
        self.wait_click_item_btn(self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][role='link']"))
        self.wait3.until(EC.invisibility_of_element((username_elem)))
        # sign_out.click()

    def click_delete_user(self, btn): # ! in-class method
        try:
            self.wait3.until(EC.element_to_be_clickable((btn)))
            btn.click()
        except:
            self.click_delete_user()

    def delete_logged_user(self):
        self.click_my_account()
        # delete_account_btn = self.driver.find_element(By.CSS_SELECTOR, "#myAccountContainer>div>button")
        delete_account_btn = self.driver.find_element(By.CSS_SELECTOR, "div.deleteBtnText")
        self.click_delete_user(self.driver.find_element(By.CSS_SELECTOR, "div.deleteBtnText"))
        self.wait3.until(EC.visibility_of((self.driver.find_element(By.CSS_SELECTOR, "div[id='deleteAccountPopup']>div[class='deleteBtnContainer']>div[class='deletePopupBtn deleteRed']"))))
        self.driver.find_element(By.CSS_SELECTOR, "div[id='deleteAccountPopup']>div[class='deleteBtnContainer']>div[class='deletePopupBtn deleteRed']").click()


    def click_aos_logo(self):
        aos_logo = self.driver.find_element(By.CSS_SELECTOR, "a[href='#/']")
        self.wait10.until(EC.element_to_be_clickable(aos_logo))
        aos_logo.click()

    def click_cart(self):
        cart = self.driver.find_element(By.ID, "menuCart")
        cart.click()
        ActionChains(self.driver).move_to_element(self.user_btn).perform()
        self.user_btn.send_keys(Keys.ESCAPE)
        # waiting for cat popup to close
        self.wait10.until(EC.invisibility_of_element(((self.driver.find_element(By.CSS_SELECTOR, '#toolTipCart>div>table')))))

    def get_total_items(self):
        # !!!
        # sleep(3)
        amount_str = self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink>span").text
        if amount_str == '':
            return 0
        return int(amount_str)

    ## POP-UP CART METHODS ##

    def get_items_from_popup_cart(self):
        if self.get_total_items() != 0:
            # toolTipCart>div>table>tbody>tr
            # [{name:'' ,quant:'', color:''}, {name:'' ,quant:'', color:''}...]
            self.show_cart_popup()
            items = []
            rows = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
            for row in rows:
                cart_items = row.find_elements(By.XPATH, ".//td[2]/a")  # parent: h3(name), label(quant), label>span(color)
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

    def get_items_elems_from_popup_cart(self):
        if self.get_total_items() != 0:
            self.show_cart_popup()
            items_elems = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
            items_elems.reverse()
            return items_elems
        else:
            print("The cart is empty")
            return []


    def remove_item_from_popup_cart(self, item_index):
        # .closeDiv
        self.show_cart_popup()
        items_before = self.get_items_elems_from_popup_cart()
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#toolTipCart>div>table>tbody>tr")
        remove_btn = rows[item_index].find_element(By.CSS_SELECTOR, ".closeDiv>div")
        remove_btn.click()
        items_after = self.get_items_elems_from_popup_cart()
        removed_item = [item for item in items_before if item not in items_after]
        return removed_item


    ## function referring to location in the site ##

    def get_page(self):
        # div>nav
        path = self.driver.find_elements(By.CSS_SELECTOR, "nav>a")
        if len(path) == 0:
            return "Home"
        else:
            return path[len(path)-1].text

    def go_back(self):
        self.driver.back()