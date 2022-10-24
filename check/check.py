from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service('C:\Driver\chromedriver_win32\chromedriver.exe'))
driver.get("https://www.google.com/")
print(driver.title)
element = driver.find_element("name", "q")
element.send_keys("Niloy")
element.submit()
print(driver.title)
