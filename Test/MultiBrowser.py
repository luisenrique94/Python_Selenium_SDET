from  selenium import  webdriver
from  selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("https://www.glideapps.com/")
print(driver.title) #obtienes el titulo de la pagina
print(driver.current_url) #obtienes la url de la pagina
print(driver.page_source) #obtenienes el  codigo html de lap gina
driver.close()
