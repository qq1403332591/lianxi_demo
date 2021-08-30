from action_chains.po_page.index_page import Index


class TestCase():

    def setup_class(self):
        self.index = Index()


    def test_case1(self):
        self.index.index_page().login()


    def test_case2(self):
        username = "姚3"
        user = "yao125"
        phone = "13100000105"
        index = self.index.add_person()
        index.add_contact(username,user,phone)
        assert username in index.verify_person_exist_list(username)

    def teardown_class(self):
        self.index.driver.quit()


