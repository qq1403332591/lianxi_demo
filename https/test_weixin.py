import json

import requests


class Test_WeiXin():
    def test_get_biaoqian(self):
        corpsecret = '-Pvw3PqU_ylhpj75VroMnqOfRW5pXJfsLguXMuqemQg'
        corpid = "wwafa879921b0e5a41"
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={"corpid": corpid, "corpsecret": corpsecret
                                 }
                         )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']


        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": token},
            json={
                "tag_id":[]
            }
        )
        print(json.dumps(r.json(), indent=2))  # 将python对象编码成Json字符串
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
