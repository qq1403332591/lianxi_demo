import yaml
from selenium.webdriver.common.by import By

from frame.search import SearCh
from frame.base_page import BasePage


class Base_Main(BasePage):
    def goto_market(self):
        # 制造假的弹窗
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()


        '''
        with open("market.yaml",encoding="utf-8") as f:
            data = yaml.load(f)
            func = data["goto_market"]
        for ele in func:
            if "click" == ele["action"] :  # 当action是click的时候
                self.find(ele["by"],ele["locator"]).click()   # 去查找他的元素并且点击

        '''

        self.open_yaml("./market.yaml","goto_market")
        return SearCh(self.driver)