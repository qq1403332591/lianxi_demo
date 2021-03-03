from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page():
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)


    def find_element(self,by,locator=None):
        if locator == None:
            res: WebElement = WebDriverWait(self.driver,10).until(lambda x: x.find_element(*by))
            return res
        else:
            res: WebElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by,locator))
            return res

    def finds(self,locator):
        return  self.driver.find_elements(*locator)
