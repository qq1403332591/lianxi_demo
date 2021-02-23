import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCase:
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222" # 终端运行Google\ Chrome --remote-debugging-port=9222
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_case1(self):
        #  使用复用浏览器的方法获取到cookies，将cookies保存下来。
        # cookies = self.driver.get_cookies()
        cookies = [{'***'}]
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for num in cookies:
            self.driver.add_cookie(num)  # 因为addcookie需要传入字典，我们拿到的cookies是一个列表。
        self.driver.refresh()  # 刷新网页
        time.sleep(5)

    def teardown(self):
        self.driver.quit()


