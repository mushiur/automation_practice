import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Test1:
    def __init__(self):
        self.time = None
        self.driver = None

    def setup_method(self):
        s = Service('C:\Driver\chromedriver_win32\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test_1(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def sign_in(self):
        self.driver.find_element("xpath", "//a[@class='login']").click()

    def email_field(self, a):
        self.driver.find_element("id", "email_create").send_keys(a)
        self.driver.find_element("xpath", "//button[@id='SubmitCreate']").click()

    def personal_information(self, fs_name, ls_name, ps_w):
        self.driver.find_element("xpath", "//input[@id='id_gender1']").click()
        self.driver.find_element("id", "customer_firstname").send_keys(fs_name)
        self.driver.find_element("id", "customer_lastname").send_keys(ls_name)
        self.driver.find_element("id", "passwd").send_keys(ps_w)

    def dob(self, days, month, year):
        element_d = self.driver.find_element("id", "days")
        element_d.send_keys(days)
        element_m = self.driver.find_element("id", "months")
        element_m.send_keys(month)
        element_y = self.driver.find_element("id", "years")
        element_y.send_keys(year)
        self.driver.find_element("xpath", "//input[@id='newsletter']").click()
        self.driver.find_element("xpath", "//input[@id='optin']").click()

    def y_address(self, o_ad, o_city, o_state, post_code, o_mobile):
        self.driver.find_element("id", "company")
        self.driver.find_element("id", "address1").send_keys(o_ad)
        element_c = self.driver.find_element("id", "city")
        element_c.send_keys(o_city)
        element_s = self.driver.find_element("id", "id_state")
        element_s.send_keys(o_state)
        self.driver.find_element("id", "postcode").send_keys(post_code)
        element_phone = self.driver.find_element("id", "phone_mobile")
        element_phone.send_keys(o_mobile)
        element_address = self.driver.find_element("id", "alias")
        element_address.send_keys(" is given")
        self.driver.find_element("xpath", "//button[@id='submitAccount']").click()

    def search_box(self):
        element = self.driver.find_element("id", "search_query_top").send_keys("Shirt")
        self.driver.find_element("xpath", "//button[@name='submit_search']").click()
        self.driver.implicitly_wait(20)

    def add_cart(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element("xpath", "//span[normalize-space()='Add to cart']").click()
        self.driver.implicitly_wait(20)

    def pro_checkout(self):
        self.driver.find_element("xpath", "//span[normalize-space()='Proceed to checkout']").click()
        self.driver.find_element("xpath", "//*[@id='center_column']/p[2]/a[1]/span").click()
        self.driver.find_element("xpath", "//*[@id='center_column']/form/p/button/span").click()
        self.driver.find_element("xpath", "//input[@id='cgv']").click()
        self.driver.find_element("xpath", "//*[@id='form']/p/button/span").click()

    def quit(self):
        print("Done")
        self.driver.quit()


test1 = Test1()
test1.setup_method()
test1.test_1()
test1.sign_in()
test1.email_field("xsds21st@gmail.com")
test1.personal_information("rifa", "ra", "Robi@123")  # first name, last name , password
test1.dob(12, "February", 1997)
test1.y_address("12/2,Gulshan,Red.dot", "Chicago", "Florida", "33034", "01876006208")
test1.search_box()
test1.add_cart()
test1.pro_checkout()
# test1.quit()
