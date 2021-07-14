from action_chains.po_page.index_page import Index


class TestCase():

    def setup_class(self):
        self.index = Index()


    def test_case1(self):
        self.index.index_page().login()


    def test_case2(self):
        username = "打算1"
        user = "13100dasuan1"
        phone = "13100000010"
        index = self.index.add_person()
        index.add_contact(username,user,phone)
        assert username in index.verify_person_exist_list()

    def teardown_class(self):
        self.index.driver.quit()
