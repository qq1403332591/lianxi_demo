import datetime

import pytest
from jsonpath import jsonpath

from https.tag import Tag


class Test_WeiXin():
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("name,id", [
        ['tag', 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ'],
        ['tag-1', 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ'],
        ['ABC', 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ']
    ])
    def test_get_biaoqian(self, name, id):
        name = name + str(datetime.datetime.now())[11:19]
        # id = 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ'
        self.tag.list()
        self.tag.updata(id=id,
                        name=name)
        r = self.tag.list()
        # tags = [tar_num for num in r.json()['tag_group'] if num['group_name'] == 'python15'
        #         for tar_num in num['tag']
        #         if tar_num['name'] == name]
        # assert len(tags) != 0
        assert jsonpath(r.json(), f"$..[?(@.name=='{name}')]")[0]['name'] == name
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    # 如果40071,"UserTag Name Already Exist用户标签名已经存在
    # 1.删除对应的tag
    # 2.已有的tag_name的基础上追加名字
    def test_add_biaoqian(self):
        group_data = "test1225"
        tag_data = [{
            "name": "tag_1225_01"
        },
            {
                "name": "tag_1225_02"
            }
        ]
        self.tag.add(group_name=group_data,tag=tag_data)

    def test_list(self):
        r = self.tag.list()




    # 40068 ："invalid tagid, 非法的tag_id，(tag_id不存在，重复删除的情况)
    # 几种接口情况：
    # 0.手动添加一个接口，再删除
    # 1.删除接口有问题
    # 2.反复验证，再进行重试，重复次数：n次 ：手动实现，借助pytest 钩子（rerun插件）
    #   a, 添加一个接口，
    #   b，对添加的接口再删除
    #   c, 查询接口是否删除成功
    def test_delect(self):
        tagid = ["etXT2CDwAAq4aUjQFpUjXel257exNZwg"]
        self.tag.delect_group_id(tagid)


    def test_beforadd(self):
        group_data = "tmp12345"
        tag_data = [{
            "name": "t1"
        },
            {
                "name": "t2"
            }
        ]
        group_id = self.tag.bef_add(group_data,tag_data)
        print("***************************")
        for num in self.tag.list().json()['tag_group']:
            if num['group_id'] == group_id:
                assert True




    def test_befor_delect(self):
        r = self.tag.before_delect(['etXT2CDwAApKQWaY8U4JDvmUvxciZJkA'])
        assert r.json()['errcode'] == 0

    def test_update(self):
        self.tag.updata('etXT2CDwAA9Gw7FOArjj0XS_U54f5Z3Q','abcd')