from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page():
    def __init__(self,driver=None):
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"  # 终端运行Google\ Chrome --remote-debugging-port=9222 chrome --remote-debugging-port=9222
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

        else:
            self.driver = driver

    def find_element(self,by:None,locator):
        if by is None:
            res:WebElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
            return res
        else:
            res:WebElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by,locator))
            return res