from selenium.webdriver.common.by import By

from frame.InputSearch import InputSearch
from frame.base_page import BasePage


class SearCh(BasePage):
    def go_search(self):
        self.find(By.ID,'com.xueqiu.android:id/action_search').click()
        return  InputSearch(self.driver)

