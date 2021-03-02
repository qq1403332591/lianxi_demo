from selenium.webdriver.remote.webdriver import WebDriver

from selenium_demo.po_demo2.page.base_page import Base_Page


class Contact_Page(Base_Page):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def send_contact(self,username,number,mobilie):
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_name('acctid').send_keys(number)
        self.driver.find_element_by_id('memberAdd_phone').send_keys(mobilie)
        self.driver.find_element_by_xpath('//*[@class="qui_btn ww_btn js_btn_save"]').click()
        return True


    def verify(self):
        # 验证添加结果
        res = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        # num_list = []
        # for num in res:
        #     num_list.append(num.get_attribute('title'))
        num_list = [num.get_attribute('title') for num in res]
        return  num_list



