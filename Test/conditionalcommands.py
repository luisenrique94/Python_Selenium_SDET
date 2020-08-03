from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
name=driver.find_element_by_xpath("//input[@placeholder='First Name']")
print(name.is_displayed()) #retorna true o false
print(name.is_enabled()) #retornar true o false
lastname = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
print(lastname.is_displayed())
print(lastname.is_enabled())
name.send_keys("luis")
lastname.send_keys("chavez")

radio1 = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
radio2 = driver.find_element_by_xpath("//label[2]//input[1]")
print(radio1.is_selected())
print(radio2.is_selected())