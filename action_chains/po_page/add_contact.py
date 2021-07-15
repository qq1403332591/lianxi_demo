import time

from selenium.webdriver.chrome.webdriver import WebDriver

from action_chains.po_page.base_page import Base_Page


class AddContact(Base_Page):



    def add_contact(self,username,user,phone):

        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('memberAdd_acctid').send_keys(user)
        self.driver.find_element_by_id('memberAdd_phone').send_keys(phone)
        # js = "window.scrollTo(10000,10000)"
        # self.driver.execute_script(js)
        # driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.find_element_by_css_selector('.member_colRight_operationBar a:nth-child(2)').click()

    def verify_person_exist_list(self,value):  # 验证联系人存在列表中

        person_title_total_list = []
        while True:
            perpon = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_tr td:nth-child(2)')
            person_title_list = [name.get_attribute('title') for name in perpon]
            print(person_title_list)
            if value in person_title_list:
                print(person_title_list)
                return person_title_list
            person_title_total_list += person_title_list

            num:str = self.driver.find_element_by_xpath('//*[@class="ww_pageNav js_page_container"]/div[1]/div[1]').text
            num1,num2 = num.split('/',1)
            if num1 != num2:
                self.driver.find_element_by_xpath('//*[@class="ww_pageNav_info"]/a[2]').click()
            else:
                return False
        return person_title_total_list




