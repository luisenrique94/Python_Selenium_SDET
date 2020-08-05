from selenium import webdriver
def chrome(self):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://sandbox.chazki.com/#/login")



