from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.implicitly_wait(10)

print(driver.title)
flight=driver.find_element_by_xpath("//span[contains(text(),'Flights')]").click()

origen = driver.find_element_by_xpath("//*[@id='wizard-flight-tab-roundtrip']/div/div[1]/div/div[1]/div/div/div/button").click()
#origen_data= driver.find_element_by_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/header/section/div/input")
#origen_data.click()
#origen_data.send_keys("Lima", Keys.DOWN, Keys.ENTER)
time.sleep(5)

