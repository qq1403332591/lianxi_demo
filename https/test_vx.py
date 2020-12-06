import datetime
import json

import requests


class Test_WeiXin():
    def test_get_biaoqian(self):
        # 1.获取token
        corpsecret = '-Pvw3PqU_ylhpj75VroMnqOfRW5pXJfsLguXMuqemQg'
        corpid = "wwafa879921b0e5a41"
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={"corpid": corpid, "corpsecret": corpsecret
                                 }
                         )
        # print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # 2.获取企业标签库
        token = r.json()['access_token']
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": token},
            json={
                "tag_id": []
            }
        )
        # print(json.dumps(r.json(), indent=2))  # 将python对象编码成Json字符串
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # 3.编辑企业客户标签
        id = 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ'
        name = 'tag' + str(datetime.datetime.now())[11:19]
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                          params={"access_token": token},
                          json={
                              "id": id,
                              "name": name
                          })
        # print(json.dumps(r.json(), indent=2))  # 将python对象编码成Json字符串
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # 4.重新获取企业标签库，目的是验证第三步修改的name值是否生效,作断言用
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": token},
            json={
                "tag_id": []
            }
        )

        # for表达式最终的返回是列表
        tags = [tar_num for num in r.json()['tag_group'] if num['group_name'] == 'python15'
                for tar_num in num['tag']
                if tar_num['name'] == name]
        assert len(tags) != 0
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
