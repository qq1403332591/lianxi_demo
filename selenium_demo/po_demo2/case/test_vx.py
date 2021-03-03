import time

from selenium_demo.po_demo2.page.weixin_index import Index_Page


class Test_Vxcase():
    def setup(self):
        self.index = Index_Page()


    def test_add_contact(self):
        username = '张37'
        number = '13111111125'
        mobilie = '13111111125'
        ele = self.index.add_contact()
        ele.send_contact(username,number,mobilie)
        time.sleep(1)
        assert  username in ele.verify(username)


