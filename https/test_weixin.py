import datetime

from jsonpath import jsonpath

from https.tag import Tag


class Test_WeiXin():
    def test_get_biaoqian(self):
        name = 'tag' + str(datetime.datetime.now())[11:19]
        id = 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ'
        tag = Tag()
        tag.list()
        tag.updata(id=id,
                   name=name)
        r = tag.list()
        # tags = [tar_num for num in r.json()['tag_group'] if num['group_name'] == 'python15'
        #         for tar_num in num['tag']
        #         if tar_num['name'] == name]
        # assert len(tags) != 0
        assert jsonpath(r.json(), f"$..[?(@.name=='{name}')]")[0]['name'] == name
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
