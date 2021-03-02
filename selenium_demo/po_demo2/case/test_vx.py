from selenium_demo.po_demo2.page.weixin_index import Index_Page


class Test_Vxcase():
    def setup(self):
        self.index = Index_Page()


    def test_add_contact(self):
        username = 'a10'
        number = '13153117121'
        mobilie = '13153117121'
        ele = self.index.add_contact()
        ele.send_contact(username,number,mobilie)
        assert  username in ele.verify()
