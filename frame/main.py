from selenium.webdriver.common.by import By

from frame.Search import SearCh
from frame.base_page import BasePage


class Base_Main(BasePage):
    def goto_market(self):
        # 制造假的弹窗
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return SearCh(self.driver)