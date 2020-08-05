from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)
assert "Register" in driver.title
print(driver.title)
name=driver.find_element_by_xpath("//input[@placeholder='First Name']")
lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']")

name.send_keys("luis")
lastname.send_keys("chavez")
