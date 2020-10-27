import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestCase:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.implicitly_wait(3)


    def test_click(self):
        el1 = self.driver.find_element(By.XPATH,"//*[@value='dbl click me']")
        el2 = self.driver.find_element(By.XPATH,"//*[@value='click me']")
        el3 = self.driver.find_element(By.XPATH,"//*[@value='right click me']")
        actionchains = ActionChains(self.driver)
        actionchains.click(el2)
        actionchains.context_click(el3)
        actionchains.double_click(el1)
        time.sleep(3)
        actionchains.perform()

    def tear_down(self):
        self.driver.quit()

