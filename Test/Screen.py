from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("https://sandbox.chazki.com/#/login")
#driver.save_screenshot("C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Screen\\home.png")
driver.get_screenshot_as_file("C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Screen\\home.png")