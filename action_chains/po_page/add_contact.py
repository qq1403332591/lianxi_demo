import time


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

    def verify_person_exist_list(self):  # 验证联系人存在列表中
        time.sleep(2)
        person_title_list = []
        while True:
            perpon = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_tr td:nth-child(2)')
            for name in perpon:
                person_title = name.get_attribute('title')
                person_title_list.append(person_title)

            num:str = self.driver.find_element_by_xpath('//*[@class="ww_pageNav js_page_container"]/div[1]/div[1]').text
            num1,num2 = num.split('/',1)
            if num1 != num2:
                self.driver.find_element_by_xpath('//*[@class="ww_pageNav_info"]/a[2]').click()
                perpon1 = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_tr td:nth-child(2)')
                for name1 in perpon1:
                    person_title1 = name1.get_attribute('title')
                    person_title_list.append(person_title1)
            break
        return person_title_list



