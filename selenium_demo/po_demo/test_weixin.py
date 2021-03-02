from selenium_demo.po_demo.index_page import Index_Page


class Test_Weixin():
    def setup(self):
        self.index = Index_Page()



    def test_case1(self):
        # assert  self.index.goto_login().register().send_register()
        assert  self.index.go_register().send_register()

