from selenium import webdriver
import time


class TestCase():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.12306.cn/index/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_riqi(self):
        ele = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        time.sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
        self.driver.execute_script('document.documentElement.scrollTop=1000')  # 向下滚动
        time.sleep(3)
