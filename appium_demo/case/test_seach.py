from appium_demo.page.mainpage import MainPage


class TestCase:

    def setup_class(self):
        self.main = MainPage()

    def test_search(self):
        self.main.goto_hangqing().seach()



