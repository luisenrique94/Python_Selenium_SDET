import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time
sys.path.append("C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET")
from  pageObjects.LoginPage import LoginPage
class LoginTest(unittest.TestCase):
    baseURL= "https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPasswrod(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title is not matching")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
      unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Reports"))
