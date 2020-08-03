from  selenium import  webdriver
from  selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

driver.get("http://www.pavantestingtools.com/")
time.sleep(5)
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)