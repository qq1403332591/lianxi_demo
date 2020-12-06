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
