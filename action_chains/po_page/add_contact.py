from selenium.webdriver.remote.webdriver import WebDriver


class AddContact():
    def __int__(self,driver:WebDriver):
        self.driver = driver


    def add_contact(self,username,user,phone):
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('memberAdd_acctid').send_keys(user)
        self.driver.find_element_by_id('memberAdd_phone').send_keys(phone)
        self.driver.find_element_by_css_selector('.member_colRight_operationBar a:nth-child(2)').click()