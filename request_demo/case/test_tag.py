from jsonpath import jsonpath
from string import Template
from request_demo.page.tag import Page_Tag


class Test_Tag():
    def setup(self):
        self.tag = Page_Tag()

    def test_get_enterprise_label(self):
        r = self.tag.get_enterprise_label()
        # print(r.json()['errmsg'])

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


    def test_stringTemplate(self):
        # 创建一个Template实例tmp
        tmp = Template("I have ${yuan} yuan,I can buy ${how} hotdog")
        yuanList = [1, 5, 8, 10, 12, 13]
        for yu in yuanList:
            # substitute()按照Template中string输出
            # 并给相应key赋值
            Substitute = tmp.substitute(yuan=yu, how=yu)
            print(Substitute)

    def test_demo(self):
        sql = Template("")
        yuanlist = [1,10,20]
        for yu in yuanlist:
            num = sql.substitute(id=yu)
            print(num)


    def test_demo01(self):
        '''
        字符串模板
        :return:参考帖子
        https://www.jb51.net/article/119293.htm
        '''
        num = self.tag.open_yaml('find_news_id')
        sql = Template(num)
        id_list = [1]
        print(sql.substitute(id=id_list[0]))