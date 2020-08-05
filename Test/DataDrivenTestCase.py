from Test import  XLUtils
from  selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("https://sandbox.chazki.com/#/login")
driver.maximize_window()
path = "C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Data\\Login.xlsx"

rows = XLUtils.getRowCount(path,'Hoja1')

for r in range (2, rows+1):
    username=XLUtils.readData(path, "Hoja1",r,1)
    password=XLUtils.readData(path,"Hoja1",r,2)

    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[1]/span/input").clear()
    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[1]/span/input").send_keys(username)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[2]/span/input").send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[3]/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@id='menu-button']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//i[@class='material-icons'][contains(text(),'keyboard_arrow_down')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(),'Salir')]").click()
    if driver.title=="Ataribox":
        print("test is passed")
        XLUtils.writeData(path, "Hoja1", r,3, "test passed")
    else:
        print("test failed")
        XLUtils.writeData(path, "Hoja1", r, 3, "test failed")