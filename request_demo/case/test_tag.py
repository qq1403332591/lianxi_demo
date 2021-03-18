from jsonpath import jsonpath

from request_demo.page.tag import Page_Tag


class Test_Tag():
    def setup(self):
        self.tag = Page_Tag()

    def test_get_Enterprise_label(self):
        r = self.tag.get_Enterprise_label()
        print(r.json()['errmsg'])

    def test_edit_tag(self):
        tagname = 'NEW_TAG_NAME'
        r = self.tag.exit_tag()
        res = self.tag.get_Enterprise_label()
        # tag_list = [tag for tags in res.json()['tag_group'] if tags['group_name'] == 'tmp12345' for tag in tags['tag']
        #             if tag['name'] == tagname]
        # assert len(tag_list) != 0

        # jsonpath(res.json(), f"$..[?(@.name=='{tagname}')]")[0]['name']  取出tagname所在的整个列表
        assert jsonpath(res.json(), f"$..[?(@.name=='{tagname}')]")[0]['name'] == tagname

    def test_add_tag(self):
        tag1 = 'TAG_NAME_5'
        tag2 = 'TAG_NAME_6'
        tag1_id = []
        r = self.tag.add_tag(tag1, tag2)
        res = self.tag.get_Enterprise_label()
        for num in res.json()['tag_group']:
            if num['group_name'] == 'GROUP_NAME':
                for tag_id in num['tag']:
                    if tag_id['name'] ==  tag1:
                        tag1_id.append(tag_id['id'])
                    elif tag_id['name'] == tag2:
                        tag1_id.append(tag_id['id'])
        if tag1 == jsonpath(self.tag.get_Enterprise_label().json(),f"$..[?(@.name=='{tag1}')]")[0]['name']:
            self.tag.delect_tag(tag1_id[0])



        # print(jsonpath(res.json(), f"$..[?(@.name=='{tag1}')]"))
