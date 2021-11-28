from wechat_web.mianpage import MainPage


class TestCase():

    def test_add_contacts(self):
        main = MainPage()
        main.goto_contacts().add_contacts().exist_add_contacts()