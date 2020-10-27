import time
import pytest
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestCase:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.implicitly_wait(3)

    @pytest.mark.skip
    def test_click(self):  # 点击事件
        el1 = self.driver.find_element(By.XPATH,"//*[@value='dbl click me']")
        el2 = self.driver.find_element(By.XPATH,"//*[@value='click me']")
        el3 = self.driver.find_element(By.XPATH,"//*[@value='right click me']")
        actionchains = ActionChains(self.driver)
        actionchains.click(el2)
        actionchains.context_click(el3)  # 双击
        actionchains.double_click(el1)  # 右击
        time.sleep(3)
        actionchains.perform()



    def test_dragdrop(self):  # 拖动释放
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        el1 = self.driver.find_element_by_id('dragger')
        el2 = self.driver.find_element_by_xpath('/html/body/div[2]')
        actionchains = ActionChains(self.driver)
        actionchains.drag_and_drop(el1,el2)    # 然后移动到目标元素并释放鼠标按钮。
        actionchains.perform()
        time.sleep(3)


    def teardown(self):
        self.driver.quit()