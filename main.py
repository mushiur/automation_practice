import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

first_name = "Rifat"
last_name = "Rahman"
email = "ri70091@mail.com"
password = "Robi@12345"
company = "Red.dot"
address = "12/2,Gulshan,Red.dot"
address2 = "Protik , 4th floor, 4-B"
city = "Chicago"
state = "Florida"
zip_code = "33034"
phone = "3314443"
mobile = "01876006208"
# Chrome
# s = Service('C:\Driver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=Service('C:\Driver\chromedriver_win32\chromedriver.exe'))
driver.get("http://automationpractice.com/index.php")
print(driver.title)

driver.maximize_window()
driver.find_element("xpath", "//a[@class='login']").click()
time.sleep(1)

element = driver.find_element("id", "email_create")
element.send_keys(email)
time.sleep(1)

driver.find_element("xpath", "//button[@id='SubmitCreate']").click()
time.sleep(10)

driver.find_element("xpath", "//input[@id='id_gender1']").click()
time.sleep(1)

element = driver.find_element("id", "customer_firstname")
element.send_keys(first_name)
time.sleep(1)

element = driver.find_element("id", "customer_lastname")
element.send_keys(last_name)
time.sleep(1)

element = driver.find_element("id", "passwd")
element.send_keys(password)
time.sleep(1)

element = driver.find_element("id", "days")
element.send_keys(12)
time.sleep(1)

element = driver.find_element("id", "months")
element.send_keys("February")
time.sleep(1)

element = driver.find_element("id", "years")
element.send_keys(1997)
time.sleep(1)

driver.find_element("xpath", "//input[@id='newsletter']").click()

driver.find_element("xpath", "//input[@id='optin']").click()

'''element = driver.find_element("id", "firstname")
element.send_keys(first_name)

element = driver.find_element("id", "lastname")
element.send_keys(last_name)'''

element = driver.find_element("id", "company")
element.send_keys(company)

element = driver.find_element("id", "address1")
element.send_keys(address)

element = driver.find_element("id", "address2")
element.send_keys(address2)

element = driver.find_element("id", "city")
element.send_keys(city)

element = driver.find_element("id", "id_state")
element.send_keys(state)

element = driver.find_element("id", "postcode")
element.send_keys(zip_code)

element = driver.find_element("id", "other")
element.send_keys("Lorem ipsum blah blah")

element = driver.find_element("id", "phone")
element.send_keys(phone)

element = driver.find_element("id", "phone_mobile")
element.send_keys(phone)

element = driver.find_element("id", "alias")
element.send_keys(address)

driver.find_element("xpath", "//button[@id='submitAccount']").click()

# search shirt
element = driver.find_element("id", "search_query_top")
element.send_keys("shirt")

# search button
driver.find_element("xpath", "//button[@name='submit_search']").click()
time.sleep(2)

# add to cart
time.sleep(10)
driver.find_element("xpath", "//span[normalize-space()='Add to cart']").click()
time.sleep(10)

# proceed to checkout
driver.find_element("xpath", "//span[normalize-space()='Proceed to checkout']").click()
time.sleep(5)

driver.find_element("xpath", "//*[@id='center_column']/p[2]/a[1]/span").click()
time.sleep(2)

driver.find_element("xpath", "//*[@id='center_column']/form/p/button/span").click()
time.sleep(2)

driver.find_element("xpath", "//input[@id='cgv']").click()
time.sleep(2)
driver.find_element("xpath", "//*[@id='form']/p/button/span").click()

driver.quit()
