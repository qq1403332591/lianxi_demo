from frame.base_page import BasePage


class InputSearch(BasePage):
    def search_res(self):
        input_locator = ("id","com.xueqiu.android:id/search_input_text")
        self.find(input_locator).send_keys("小米")