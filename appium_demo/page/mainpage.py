from selenium.webdriver.common.by import By

from appium_demo.page.basepage import BasePage
from appium_demo.page.market_page import Market_Page


class MainPage(BasePage):
    def goto_hangqing(self):
        self.find(By.ID,'post_status').click()
        self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return Market_Page(self.driver)
