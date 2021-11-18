"""
מה מבנה הטסטים? האם לכל סעיף צריך להיות טסט משלו?
איך מונעים בעיית סנכון באופן גורף (למשל, אם בדיוק עברתי עמוד)? האם צריך להתחשב בבעיות סנכרון עבור כל פונקציה?

פונקציה מחזירה את פרטי המוצר שנכנס לעגלה/ נמחק מהעגלה
"""
from random import randint
from time import sleep
from unittest import TestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from Classes.TopBar_Class import Topbar
from Classes.Homepage_Class import Homepage
from Classes.Category_Class import Category
from Classes.Product_Class import Product
from Classes.Cart_Class import Cart
from Classes.OrderPayment_Class import OrderPayment
from Classes.CreateAccount_Class import CreateAccount
from Classes.MyOrders_Class import MyOrders


class test_AOS_Website(TestCase):

    def setUp(self):
        self.service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.topbar = Topbar(self.driver)
        self.homepage = Homepage(self.driver)
        self.category = Category(self.driver)
        self.product = Product(self.driver)
        self.cart = Cart(self.driver)
        self.order_payment = OrderPayment(self.driver)
        self.create_account = CreateAccount(self.driver)
        self.my_orders = MyOrders(self.driver)
        if self.topbar.is_logged_in():
            self.topbar.click_sign_out()


    ## IN-CLASS METHODS

    # goes to in-stock random product page
    def go_to_random_product(self):
        self.topbar.click_aos_logo()
        self.homepage.click_random_category()
        self.category.click_random_product()
        if self.product.is_sold_out():  # recursive call if the product is out of stock
            self.go_to_random_product()

    # receives amount and quantity of products to add to the cart. return a list of those products' details
    def add_random_products(self, amount, quantity):
        products_details = []
        for i in range(amount):
            self.topbar.click_aos_logo()
            self.go_to_random_product()
            self.product.change_quantity(quantity)
            products_details.append(
                {
                    'name': self.product.get_name(),
                    'quantity': self.str_to_num(self.product.get_quantity()),
                    'color': self.product.get_color(),
                    'price': self.str_to_num(self.product.get_price())
                })
            self.product.add_to_cart()
        return products_details

    # receives a string and returns a number (int or float)
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

    ##

    ## TESTS FUNCTIONS
    def test_1(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של לפחות שני מוצרים, בכמויות שונות (לדוגמה 2 יחידות של מוצר ראשון ו-3 יחידות של מוצר שני),
        יש לבדוק שכמות המוצרים הסופית מופיעה נכון ומדוייק בחלונית עגלת הקניות מצד ימין למעלה של המסך.
        """
        quant1 = randint(1, 10)
        quant2 = randint(1, 10)
        self.add_random_products(1, quant1)
        self.add_random_products(1, quant2)
        total_items = self.topbar.get_total_items()
        self.assertEqual(int(total_items), quant1 + quant2)

    def test_2(self):
        """
        לאחר בחירה של 3 מוצרים, בכמויות שונות,
        יש לבדוק שהמוצרים מופיעים נכון:
        כולל שם, צבע, כמות ומחיר בחלונית עגלת הקניות בצד ימין למעלה של המסך
        """
        # adding 3 random items to the cart, and getting their details
        initial_details = self.add_random_products(3, randint(1, 10))
        # getting the items details from the pop-up cart:
        cart_details = self.topbar.get_items_from_popup_cart()
        # turning the cart_details quantities into a number
        for item in cart_details:
            item['quantity'] = self.str_to_num(item['quantity'])
        print("initial details: ", initial_details)
        print("cart_details: ", cart_details)
        # taking care of case where the same product was added more than once:
        for i in range(len(initial_details) - 1):
            if initial_details[i]['name'] in initial_details[i:]:
                name = initial_details[i]['name']
                for j in range(i, len(initial_details) - 1):
                    if initial_details[j]['name'] == name:
                        new_quant = initial_details[i]['quantity'] + initial_details[j]['quantity']
                        initial_details[i]['quantity'] = new_quant
                        initial_details.pop(j)
        for i in range(len(initial_details)):
            # the name in the cart pop-up is only partial.
            self.assertIn(cart_details[i]['name'].rstrip('.'), initial_details[i]['name'])
            self.assertEqual(initial_details[i]['quantity'], cart_details[i]['quantity'])
            self.assertEqual(initial_details[i]['color'], cart_details[i]['color'])

    def test_3(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של לפחות שני מוצרים והסרה של מוצר אחד ע"י שימוש בחלונית עגלת הקניות למעלה מימין,
        יש לבדוק שהמוצר אכן נעלם מחלונית העגלה
        """
        # adding random amount of products to the cart
        self.add_random_products(randint(1, 4), randint(1, 10))

        popup_cart_before = self.topbar.get_items_elems_from_popup_cart()

        # choosing random product to remove
        random_index = randint(0, len(popup_cart_before) - 1)
        print("random product to remove: ", random_index, "amount fo products: ", len(popup_cart_before))

        removed_item = self.topbar.remove_item_from_popup_cart(random_index)

        popup_cart_after = self.topbar.get_items_elems_from_popup_cart()
        if removed_item in popup_cart_after:
            self.fail("The removed item is still in the cart")
        # compare amount of cart items after removing
        self.assertEqual(len(popup_cart_after), len(popup_cart_before) - 1)

    def test_4(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של מוצר כלשהו ומעבר למסך עגלת הקניות ע"י לחיצה על לחצן עגלת הקניות בצד ימין למעלה,
        יש לוודא מעבר לעמוד עגלת הקניות
        (ע"י בדיקת הופעת הטקסט:
        "Shopping cart"
        למעלה משמאל)
        """
        self.go_to_random_product()
        self.topbar.click_cart()
        current_page = self.topbar.get_page()
        self.assertEqual('SHOPPING CART', current_page)

    def test_5(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של 3 מוצרים בכמויות שונות ומעבר לעמוד עגלת הקניות, יש לבדוק שהסכום הכולל של ההזמנה תואם
        את מחירי המוצרים והכמויות שהוזמנו,
        עפ"י סיכום המחירים שהופיעו *בעת בחירת המוצרים*.
        בטסט זה יש להדפיס בצורה ברור, עבור כל מוצר בעגלת הקניות:
        שם המוצר, כמות המוצר, מחיר המוצר
        """
        # adding 3 random products to the cart
        random_quant = randint(4, 9)
        added_products = self.add_random_products(3, random_quant)  # randint(4, 15)
        total_price = 0
        for product in added_products:
            total_price += product['price'] * product['quantity']
            print("total_price: ", total_price)
        self.topbar.click_cart()
        cart_total = self.str_to_num(self.cart.get_total())
        print("cart_total: ", cart_total)
        self.assertEqual(total_price, cart_total)

    def test_6(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של שני מוצרים לפחות, לעבוד לעמוד עגלת הקניות ולבצע שני שינויים בכמויות של שני המוצרים.
        יש לבדוק שהשינויים משתקפים בעמוד עגלת הקניות.
        """
        # adding two random products to the cart
        added_products = self.add_random_products(randint(2, 4), randint(1, 10))
        items_amount = len(self.topbar.get_items_elems_from_popup_cart())
        self.topbar.click_cart()
        new_quantities = []
        for i in range(items_amount - 1):
            self.cart.click_edit(i)
            current_quant = added_products[i]['quantity']
            new_quant = randint(1, current_quant) + randint(current_quant + 1, current_quant + 5)
            new_quantities.append(new_quant)
            self.product.change_quantity(new_quant)
            self.product.add_to_cart()
        # cart_new_quantities = self.str_to_num(self.cart.get_products_quantities())
        cart_new_quantities = []
        for quantity in self.cart.get_products_quantities():
            cart_new_quantities.append(self.str_to_num(quantity))

        for i in range(len(cart_new_quantities)):
            self.assertEqual(new_quantities[i], cart_new_quantities[i])

    def test_7(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של מוצר מסוג טאבלט,
        יש לחזור אחורה ולבדוק שחזרנו למסך מוצרי ה- טאבלטים,
        ושוב לחזור אחורה ולבדוק שחזרנו למסך הראשי
        """
        self.homepage.click_specific_category("tablets")
        self.category.click_random_product()
        self.topbar.go_back()
        self.assertEqual(self.topbar.get_page(), "TABLETS")
        self.topbar.go_back()
        self.assertEqual(self.topbar.get_page(), 'Home')

    def test_8(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירת מוצרים כלשהם לקנייה, לבצע checkout,
        למלא פרטי משתמש חדש ,
        לבצע תשלום באמצעות SafePay,
        לבדוק שהתשלום בוצע בהצלחה,
        לבדוק שעגלת הקניות ריקה,
        ושההזמנה נמצאת ברשימת ההזמנות של המשתמש.
        """
        # adding 1-4 random products to the cart
        self.add_random_products(randint(1, 5), randint(3, 10))

        self.topbar.click_cart()
        self.cart.click_checkout()
        self.order_payment.click_registration()
        # creating a new account
        self.create_account.set_username('NewUser12345')
        self.create_account.set_password('Pa55w.rd', True)
        self.create_account.set_email('something@try.abc')
        self.create_account.check_i_agree()
        self.create_account.click_register()
        # dealing with checkbox not marked
        try:
            self.order_payment.click_next()
        except:
            print("user already exists")

        # entering 'Safepay' account details
        self.order_payment.set_safepay_username('SafeUser123')
        self.order_payment.set_safepay_password('SafePay1234')
        self.order_payment.click_pay_now_safepay()

        # getting the order number after it's been successfully committed
        order_number = self.order_payment.get_order_number()

        # checking if the cart is empty
        self.topbar.click_cart()
        if not self.cart.is_cart_empty():
            self.fail("The cart is not empty after committing an order.")

        # getting all of the orders numbers from 'My Orders' page.
        self.topbar.click_my_orders()
        orders_numbers = self.my_orders.get_orders_numbers()

        # checking if the recent order exists in 'My Orders' page.
        if order_number not in orders_numbers:
            self.fail(f"The order {order_number} is not in 'My Orders' page.")

        # deleting the user -> not 100% working
        print("@@@ DELETING THE ACCOUNT. THIS IS NOT PART OF THE TEST @@@")
        self.topbar.delete_logged_user()

    def test_9(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירת מוצרים כלשהם לקניה, לבצע checkout,
        להחתבר למשתמש קיים,
        לבצע תשלום באמצעות כרטיס אשראי,
        לבדוק שעגלת הקניות ריקה 
        ושההזמנה נמצאת ברשימה ההזמנות של המשתמש
        """
        # adding 1-4 random products to the cart
        self.add_random_products(randint(1, 5), randint(3, 10))

        self.topbar.click_cart()
        self.cart.click_checkout()

        # logging in to an existing account:
        self.order_payment.set_username("NewUser1234")
        self.order_payment.set_password("Pa55w.rd")
        self.order_payment.click_login()

        self.order_payment.click_next()

        # selecting 'MasterCard' payment method
        self.order_payment.select_mastercard()

        # generating random mastercard details and setting them
        # card number:
        card_number = ''
        for i in range(14):
            card_number += str(randint(0, 10))

            # CVV number
        cvv_number = randint(100, 1000)
        # cardholser name = username
        cardholder_name = self.topbar.get_username()

        # setting the details
        self.order_payment.set_mastercard_card_number(card_number)
        self.order_payment.set_mastercard_cvv_number(cvv_number)
        self.order_payment.set_mastercard_cardholder_name(cardholder_name)

        self.order_payment.click_pay_now_mastercard()

        # getting the order number after it's been successfully committed
        order_number = self.order_payment.get_order_number()

        # checking if the cart is empty
        self.topbar.click_cart()
        if not self.cart.is_cart_empty():
            self.fail("The cart is not empty after committing an order.")

        # getting all of the orders numbers from 'My Orders' page.
        self.topbar.click_my_orders()
        orders_numbers = self.my_orders.get_orders_numbers()

        # checking if the recent order exists in 'My Orders' page.
        if order_number not in orders_numbers:
            self.fail(f"The order {order_number} is not in 'My Orders' page.")

    def test_10(self):
        self.topbar.click_aos_logo()
        """
        לבדוק תהליכי התחברות והתנתקות:
        לבצע התחברות למערכת באמצעות משתמש קיים ולוודא שהחיבור הצליח
        לבצע התנתקות ולוודא שההתנתקות הצליחה
        """
        if self.topbar.is_logged_in():
            self.topbar.click_sign_out()
        self.topbar.login('NewUser1234', 'Pa55w.rd')
        self.assertTrue(self.topbar.is_logged_in())
        self.topbar.click_sign_out()
        self.assertFalse(self.topbar.is_logged_in())

