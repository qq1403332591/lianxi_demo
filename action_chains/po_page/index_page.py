from selenium import webdriver


from action_chains.po_page.login_page import Login_Page


class Index():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def index_page(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element_by_xpath("//*[@class='index_top_operation']/a[1]").click()
        return Login_Page(self.driver)


