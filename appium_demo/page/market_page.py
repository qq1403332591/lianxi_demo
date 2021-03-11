from selenium.webdriver.common.by import By

from appium_demo.page.basepage import BasePage
from appium_demo.page.seach_page import Seach_Page


class Market_Page(BasePage):
    def seach(self):
        locator = ('id','action_search')
        self.find(locator).click()
        return Seach_Page(self.driver)
