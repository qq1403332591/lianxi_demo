import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo.po_demo2.page.base_page import Base_Page


class Contact_Page(Base_Page):


    def send_contact(self,username,number,mobilie):
        self.find_element('id','username').send_keys(username)
        self.find_element('name','acctid').send_keys(number)
        self.find_element('id','memberAdd_phone').send_keys(mobilie)
        self.find_element('xpath','//*[@class="qui_btn ww_btn js_btn_save"]').click()
        return True


    def verify(self,value):
        # 验证添加结果
        # localtor = (By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # res = self.finds(localtor)
        #res = WebDriverWait(self.driver,20).until(lambda x: x.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)'))
        # num_list = []
        # for num in res:
        #     num_list.append(num.get_attribute('title'))
        num_total_title_list = []
        while True:
            localtor = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            res = self.finds(localtor)
            num_list = [num.get_attribute('title') for num in res]
            num_total_title_list += num_list

            if value in num_total_title_list:
                return num_total_title_list

            page:str = self.find_element(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            present_num,total_num = page.split("/",1)

            if int(present_num) == int(total_num):
                return False
            else:
                self.find_element(By.CSS_SELECTOR,'.ww_commonImg_PageNavArrowRightNormal').click()



            








