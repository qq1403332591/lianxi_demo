from selenium.webdriver.remote.webdriver import WebDriver


class Login_Page():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def saoma(self):
        pass


    def register(self):
        self.driver.find_element_by_class_name('login_registerBar_link').click()
        return Register_Page()



