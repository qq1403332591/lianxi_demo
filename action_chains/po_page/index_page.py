from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from action_chains.po_page.add_contact import AddContact
from action_chains.po_page.base_page import Base_Page
from action_chains.po_page.login_page import Login_Page


class Index(Base_Page):

    def index_page(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element_by_xpath("//*[@class='index_top_operation']/a[1]").click()
        return Login_Page(self.driver)



    def add_person(self):
        self.find_element(By.XPATH,'//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]/span[2]').click()
        # locator = (By.CSS_SELECTOR,'.member_colRight_operationBar a:nth-child(2)')
        # def wait_and_click(x: WebDriver):
        # 反复执行点击操作
        #     try:
        #         x.find_element(*locator)
        #         return x.find_element(*locator).click()
        #     except:
        #         False
        # WebDriverWait(self.driver,10).until(wait_and_click)
        # self.driver.find_element_by_xpath('//*[@class="index_service_cnt js_service_list"]/a[1]/div[1]/span[2]').click()
        return AddContact(self.driver)
