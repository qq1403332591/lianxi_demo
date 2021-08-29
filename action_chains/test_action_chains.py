import time

from selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Test_action_chains():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='../action_chains/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_action_keyboard_input(self):
        self.driver.get('https://sahitest.com/demo/label.htm')
        self.driver.find_element_by_xpath('/html/body/label[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/label[1]/input').send_keys('abcdaaa')
        action = ActionChains(self.driver)
        action.send_keys(Keys.SPACE).perform() # 输入空格
        action.send_keys('ccc').pause(1)
        action.send_keys(Keys.BACKSPACE).perform()   # 执行back键
        time.sleep(3)

    def teardown(self):
        self.driver.quit()


