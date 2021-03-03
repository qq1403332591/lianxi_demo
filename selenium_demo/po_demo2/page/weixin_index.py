from selenium  import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo.po_demo2.page.base_page import Base_Page
from selenium_demo.po_demo2.page.contact_page import Contact_Page


class Index_Page(Base_Page):
    def add_contact(self):
        # self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        # 点击联系人按钮
        self.find_element('id','menu_contacts').click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(By.CSS_SELECTOR,'.js_has_member>div>a:nth-child(2)').click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)
        return Contact_Page(self.driver)



