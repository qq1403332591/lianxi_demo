from action_chains.po_page.index_page import Index


class TestCase():

    def setup_class(self):
        self.index = Index()


    def test_case1(self):
        self.index.index_page().login()


    def test_case2(self):
        self.index.add_person()

    def teardown_class(self):
        self.index.driver.quit()
