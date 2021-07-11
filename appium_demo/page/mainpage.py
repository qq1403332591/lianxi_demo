import time

import yaml
from selenium.webdriver.common.by import By

from appium_demo.page.basepage import BasePage
from appium_demo.page.market_page import Market_Page


class MainPage(BasePage):
    def goto_hangqing(self):
        #self.find(By.ID,'post_status').click
        # with open('./../yamldata//goto_hangqing.yaml',encoding='utf-8') as f:
        #     yaml_data = yaml.load(f)
        # data_list = yaml_data['goto_hangqing']
        # for ele in data_list:
        #     if ele['action'] == 'click':
        #         self.find(ele['by'], ele['locator']).click()
        self.open_yaml('./../yamldata//goto_hangqing.yaml','goto_hangqing')
        self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return Market_Page(self.driver)


    def test_case02(self):
        self.driver.find_element_by_xpath('//*[@text="我的"]').click()
        self.driver.find_element_by_xpath('//*[@text="我发布的"]').click()
        while True:
            self.driver.find_element_by_xpath('//*[contains(@text,"经典落肩")]').click()
            time.sleep(1)
            self.driver.back()

