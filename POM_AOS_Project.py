"""
מה מבנה הטסטים? האם לכל סעיף צריך להיות טסט משלו?
איך מונעים בעיית סנכון באופן גורף (למשל, אם בדיוק עברתי עמוד)? האם צריך להתחשב בבעיות סנכרון עבור כל פונקציה?
"""
from random import randint
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


class test_AOS_website(TestCase):

    def setUp(self):
        self.service = Service(r'D:\QA_Course\webdrivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service= self.service)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.topbar = Topbar()
        self.homepage = Homepage()
        self.category = Category()
        self.product = Product()
        self.cart = Cart()
        self.order_payment = OrderPayment()
        self.create_account = CreateAccount()
        self.my_orders = MyOrders()

    def test_1(self):
        self.topbar.click_aos_logo()

        """
        לאחר בחירה של לפחות שני מוצרים, בכמויות שונות (לדוגמה 2 יחידות של מוצר ראשון ו-3 יחידות של מוצר שני),
        יש לבדוק שכמות המוצרים הסופית מופיעה נכון ומדוייק בחלונית עגלת הקניות מצד ימין למעלה של המסך.
        """
        quant1 = randint(1, 10)

    def test_2(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של 3 מוצרים, בכמויות שונות,
        יש לבדוק שהמוצרים מופיעים נכון:
        כולל שם, צבע, כמות ומחיר בחלונית עגלת הקניות בצד ימין למעלה של המסך
        """

    def test_3(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של לפחות שני מוצרים והסרה של מוצר אחד ע"י שימוש בחלונית עגלת הקניות למעלה מימין,
        יש לבדוק שהמוצר אכן נעלם מחלונית העגלה
        """

    def test_4(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של מוצר כלשהו ומעבר למסך עגלת הקניות ע"י לחיצה על לחצן עגלת הקניות בצד ימין למעלה,
        יש לוודא מעבר לעמוד עגלת הקניות
        (ע"י בדיקת הופעת הטקסט:
        "Shopping cart"
        למעלה משמאל)
        """


    def test_5(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של 3 מוצרים בכמויות שונות ומעבר לעמוד עגלת הקניות, יש לבדוק שהסכום הכולל של ההזמנה תואם
        את מחירי המוצרים והכמויות שהוזמנו,
        עפ"י סיכום המחירים שהופיעו *בעת בחירת המוצרים*.
        בטסט זה יש להדפיס בצורה ברור, עבור כל מוצר בעגלת הקניות:
        שם המוצר, כמות המוצר, מחיר המוצר
        """

    def test_6(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירה של שני מוצרים לפחות, לעבוד לעמוד עגלת הקניות ולבצע שני שינויים בכמויות של שני המוצרים.
        יש לבדוק שהשינויים משתקפים בעמוד עגלת הקניות.
        """


    def test_7(self):
        self.topbar.click_aos_logo()
        """
        לאחר החירה של מוצר מסוג טאבלט,
        יש לחזור אחורה ולבדוק שחזרנו למסך מוצרי ה- טאבלטים,
        ושוב לחזור אחורה ולבדוק שחזרנו למסך הראשי
        """


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


    def test_9(self):
        self.topbar.click_aos_logo()
        """
        לאחר בחירת מוצרים כלשהם לקניה, לבצע checkout,
        להחתבר למשתמש קיים,
        לבצע תשלום באמצעות כרטיס אשראי,
        לבדוק שעגלת הקניות ריקה 
        ושההזמנה נמצאת ברשימה ההזמנות של המשתמש
        """


    def test_10(self):
        self.topbar.click_aos_logo()
        """
        לבדוק תהליכי התחברות והתנתקות:
        לבצע התחברות למערכת באמצעות משתמש קיים ולוודא שהחיבור הצליח
        לבצע התנתקות ולוודא שההתנתקות הצליחה
        """

