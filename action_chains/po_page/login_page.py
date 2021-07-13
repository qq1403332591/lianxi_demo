import time

from selenium.webdriver.remote.webdriver import WebDriver


class Login_Page():
    def __init__(self,driver:WebDriver):
        self.driver = driver


    def login(self):
        self.driver.find_element_by_xpath("//*[@class='login_registerBar']/a").click()