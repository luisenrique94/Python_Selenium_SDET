from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) #obtienes el titulo de la pagina
print(driver.current_url) #obtienes la url
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
#driver.close() #navegador actualmente enfocado
driver.quit() #cierra todo el navegador


