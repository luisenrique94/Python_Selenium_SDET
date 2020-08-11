from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
@allure.severity(allure.severity_level.NORMAL)
class TestHRM():
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()
    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skippin test...Later i will implement..")
    @allure.severity(allure.severity_level.NORMALgi )
    def test_Login(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_SDET\\Drivers\\chromedriver.exe")

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        act_title= self.driver.title
        if act_title=="OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert  False

