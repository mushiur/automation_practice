import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

first_name = "Rifat"
last_name = "Rahman"
email = "rifat152015@gmail.com"
password = "Robi@12345"
# Chrome
# s = Service('C:\Driver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=Service('C:\Driver\chromedriver_win32\chromedriver.exe'))
driver.get("http://automationpractice.com/index.php")
print(driver.title)

driver.find_element("xpath", "//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
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
'''
driver.find_element("xpath", "//*[@id='input-newsletter-yes']").click()
time.sleep(1)

driver.find_element("xpath", "//*[@id='form-register']/div/div/div/input").click()
time.sleep(1)
driver.find_element("xpath", "//*[@id='form-register']/div/div/button").click()
time.sleep(3)'''

# driver.close()  # current focus browser
driver.quit()  # this will close all the browser
