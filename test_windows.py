import time

from selenium.webdriver.common.by import By
import pytest
from base import Page



class Test_Windows(Page):
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element(By.XPATH, '//*[@class="tang-pass-footerBar"]/a').click()
        time.sleep(2)
        print(self.driver.current_window_handle)  # 返回当前窗口的句柄。
        print(self.driver.window_handles)  # 返回当前会话中所有窗口的句柄
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])  # 切换窗口句柄到最后一个
        self.driver.find_element(By.NAME,"userName").send_keys("13153117137")
        time.sleep(2)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID,"TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element(By.NAME,"userName").send_keys("13153117137")
        self.driver.find_element(By.NAME,"password").send_keys("13153117137")
        self.driver.find_element(By.ID,"TANGRAM__PSP_11__submit").click()
        


