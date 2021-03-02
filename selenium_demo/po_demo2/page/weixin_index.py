from selenium  import  webdriver
from selenium.webdriver.chrome.options import Options

from selenium_demo.po_demo2.page.base_page import Base_Page
from selenium_demo.po_demo2.page.contact_page import Contact_Page


class Index_Page(Base_Page):
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    def add_contact(self):
        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        return Contact_Page(self.driver)