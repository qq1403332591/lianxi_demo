from jsonpath import jsonpath

from request_demo.page.tag import Page_Tag


class Test_Tag():
    def setup(self):
        self.tag = Page_Tag()

    def test_get_enterprise_label(self):
        r = self.tag.get_enterprise_label()
        print(r.json()['errmsg'])

    def test_edit_tag(self):
        tagname = 'NEW_TAG_NAME'
        r = self.tag.exit_tag()
        res = self.tag.get_enterprise_label()
        # tag_list = [tag for tags in res.json()['tag_group'] if tags['group_name'] == 'tmp12345' for tag in tags['tag']
        #             if tag['name'] == tagname]
        # assert len(tag_list) != 0

        # jsonpath(res.json(), f"$..[?(@.name=='{tagname}')]")[0]['name']  取出tagname所在的整个列表
        assert jsonpath(res.json(), f"$..[?(@.name=='{tagname}')]")[0]['name'] == tagname

    def test_add_tag(self):
        r = self.tag.add_tag("new1")

    def test_before_add(self):
        self.tag.find_tag_id_is_not_exist('new3')

    def test_delect_tag_id(self):
        self.tag.delect_tag(['etXT2CDwAAzvaLLqppZXO_3o9Z9fZTEQ'])


    def test_before_del(self):
        self.tag.before_del(['etXT2CDwAA0GbKyEQ11ySIjUNB5HGgrQ'])

    def test_get_list(self):
        r = self.tag.get_enterprise_label()
        for tag_group in r.json()['tag_group']:
            for tag in tag_group['tag']:
                print(tag)