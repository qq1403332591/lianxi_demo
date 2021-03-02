from selenium.webdriver.remote.webdriver import WebDriver


class Register_Page():
    def __init__(self,driver:WebDriver):
        self.driver = driver


    def send_register(self):
        self.driver.find_element_by_id('corp_name').send_keys('测试公司名称')
        self.driver.find_element_by_id('manager_name').send_keys('张三')
        self.driver.find_element_by_id('register_tel').send_keys('13153117137')
        self.driver.find_element_by_id('vcode').send_keys('123657')
        self.driver.find_element_by_id('iagree').click()
        self.driver.find_element_by_id('submit_btn').click()
        return True

