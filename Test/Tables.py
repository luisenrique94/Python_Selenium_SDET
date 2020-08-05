from  selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
print(rows)
print(cols)
for r in range(2,rows+1):
    for c in range(1, cols+1):
        datos=driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(datos, end='                ')
    print()
    time.sleep(5)

driver.close()

