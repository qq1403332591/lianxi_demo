import time

from selenium import  webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestCase:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def test_TouchActicon(self):
        """
        打开chorme
        打开url,输入senlenium，使用TouchActions.TAP点击百度一下
        搜索结果滑动


        """
        el1 = self.driver.find_element(By.ID,"kw")
        el1.send_keys('selenium')
        el2 = self.driver.find_element_by_id('su')
        touchaction = TouchActions(self.driver)
        touchaction.tap(el2)
        touchaction.perform()
        touchaction.scroll_from_element(el1,0,10000).perform()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()
