# AOS_Automation_Project

An automation project on the demo website: https://www.advantageonlineshopping.com/

- :computer:The Technologies I used for this project:
<kbd>
<img alt="Python Logo" src="https://res.cloudinary.com/practicaldev/image/fetch/s--uSnYxWbN--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://external-content.duckduckgo.com/iu/%3Fu%3Dhttps%253A%252F%252Fyourdevops.org%252Fwp-content%252Fuploads%252F2019%252F03%252Fpython3.jpg%26f%3D1%26nofb%3D1"  height="50">
</kbd>
<kbd>
  <img alt="Unittest Logo" src="https://blog.testproject.io/wp-content/uploads/2020/06/Pyunit.png" height="50">
</kbd>
<kbd>
  <img alt="Selenium Logo" src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.xmxblog.com%2Fwp-content%2Fuploads%2F2020%2F12%2Fselenium.jpg&f=1&nofb=1"  height="50">
  </kbd>
<kbd>
  <img alt="Openpyxl Logo" src="https://openpyxl.readthedocs.io/en/stable/_static/logo.png" height="40">
  </kbd>
<br>

- All of the tests are pulling data from an ["Excel" file](https://github.com/droryair/AOS_Automation_Project/blob/main/data.xlsx), and inserting the test results to a designated cell in the same file.

<h3>
  The Test Cases:
</h3>
<ol>
  <li>
    After choosing at least two products, with different quantities, checking that the total amount of products is displayed correctly in the cart pop-up on the top right corner of the website.
  </li>
  <li>
    After choosing three products, with different quantities, chicking that the products details are displayed correctly in the cart pop-up on the top right corner of the website: name, color, quantity, price.     
  </li>
  <li>
    After choosing at least three products and removing one by using the cart pop-up on the top right corner of the website, checking that the product was indeed removed from the cart pop-up.
  </li>
  <li>
    After choosing a certain product and navigating to the cart page by clicking the cart icon on the right corner of the top bar, checking succeessful navigation by the appearance of the text:"Shopping Cart" in the navigation bar on the top left. 
  </li>
  <li>
    After choosing thee products with different quantities and navigating to the cart page, checking that the total order price matches to the products quantities and prices by summing up **the prices that showed while chosing the products**. This test prints for each product in the cart: name, qunatity, price.
  </li>
  <li>
    After choosing at least two products, navigating to the cart page and make two changes in the details of the two products. Checking that the changes are being applied in the cart page.
  </li>
  <li>
    After choosing a Tablet product, going back and checking that we've returned to the Tablets category page, then going back again and checking that we've return to the Home page.
  </li>
  <li>
    After adding any products to the cart, clicking on "Checkout", filling a new user details, choosing "SafePay" payment method, checking that the payment was commited successfully, checking that the cart is empty, and that the order is displayed in the user's "Orders" page.
  </li>
  <li>
    After adding any products to the cart, clicking on "Checkout", logging in with an existing user, chossing "MasterCard" payment method, checking that the cart is empty and that the order is displayed in the user's "Orders" page.
  </li>
  <li>
    Checking logging in and logging out processes: logging in with an existing user and checking that the process was successful. Then, logging out and checking that the process was successful.
  </li>
 </ol>
