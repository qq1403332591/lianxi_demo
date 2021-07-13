from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from action_chains.po_page.login_page import Login_Page


class Index():
    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:9222"  # 终端运行Google\ Chrome --remote-debugging-port=9222 chrome --remote-debugging-port=9000
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)



    def index_page(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element_by_xpath("//*[@class='index_top_operation']/a[1]").click()
        return Login_Page(self.driver)



    def add_person(self):
        self.driver.find_element_by_xpath('//*[@class="index_service_cnt js_service_list"]/a[1]').click()
        return AddContact(self.driver)
