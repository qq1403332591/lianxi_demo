
from action_chains.po_page.base_page import Base_Page


class Login_Page(Base_Page):



    def login(self):
        self.driver.find_element_by_xpath("//*[@class='login_registerBar']/a").click()