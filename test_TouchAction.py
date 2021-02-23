import time

from selenium import  webdriver
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestCase:
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # self.driver.get("https://www.bilibili.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


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
        # scroll_from_element(on_element, xoffset, yoffset) 　　从某元素开始滚动到某个位置
        touchaction.scroll_from_element(el1,0,10000).perform()
        time.sleep(3)


    def according_to_wait(self,by,locator=None):
        if locator == None:
            return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*by))
        else:
            return WebDriverWait(self.driver,10).until(lambda x: x.find_element(by,locator))

    def test_click_and_hold(self):
        action = ActionChains(self.driver)
        atitle = self.according_to_wait(By.ID, "dragger")
        atitle2 = self.according_to_wait(By.XPATH, '//div[text()="Item 1"]')
        # 拖动元素1到元素2
        action.drag_and_drop(atitle,atitle2).perform()
        time.sleep(5)


    def scroll_find_element(self,ele):
        # 滚动查找元素
        return  self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def test_scroll_demo(self):
        ele1 = self.according_to_wait(By.XPATH, '//*[@id="bili_report_anime"]/div[2]/div[1]/header/div[1]/a')
        self.scroll_find_element(ele1)
        time.sleep(5)

    def test_fuxuan(self):
        self.according_to_wait(By.XPATH, '//*[@id="primaryChannelMenu"]/span[16]/div/a/i').click()
        time.sleep(3)
        self.driver.find_element_by_link_text("搞笑").click()

    def test_xuanzekuang(self):
        self.according_to_wait(By.XPATH,'//*[@id="select2-skill_id-container"]').click()
        time.sleep(2)
        self.according_to_wait(By.XPATH, '/html/body/span/span/span[1]/input').send_keys('驾驶飞机')
        ele1 = self.driver.find_element_by_id('select2-skill_id-result-kme1-9')

        # for i in ele1:
        #     print("start")
        #     print(i.text)
        #     print("end")
        ele1.click()
        self.driver.find_element_

    def teardown(self):
        self.driver.quit()
