from selenium  import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo.po_demo.login_page import Login_Page
from selenium_demo.po_demo.register_page import Register_Page


class Index_Page():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def find_element(self,by,locator=None):
        if locator == None:
            return WebDriverWait(self.driver,10).until(lambda x: x.find_element(*by))
        else:
            return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by,locator))


    def goto_login(self):
        self.find_element(By.CLASS_NAME,"index_top_operation_loginBtn").click()
        return Login_Page(self.driver)


    def go_register(self):
        register_locator = ("class name","index_head_info_pCDownloadBtn")
        self.find_element(register_locator).click()
        return Register_Page(self.driver)


