import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpsecret = '-Pvw3PqU_ylhpj75VroMnqOfRW5pXJfsLguXMuqemQg'
        corpid = "wwafa879921b0e5a41"
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={"corpid": corpid, "corpsecret": corpsecret
                                 }
                         )
        # print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token

    def add(self,group_name,tag):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json=
                          {
                              "group_name":group_name ,
                              "tag": tag}
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        # 2.获取企业标Tag签库
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={
                "tag_id": []
            }
        )
        print(json.dumps(r.json(), indent=2))  # 将python对象编码成Json字符串
        return r


    def updata(self, id, name):
        # id = 'etXT2CDwAAabMht1wnGAhuh0PhwpoPDQ'
        # name = 'tag' + str(datetime.datetime.now())[11:19]
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                          params={"access_token": self.token},
                          json={
                              "id": id,
                              "name": name
                          })


    def delect_group_id(self, group_id):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params=
                          {"access_token": self.token},
                          json={
                              "group_id": group_id
                          })
        print(json.dumps(r.json(), indent=2))


    def is_tag_group_name_exist(self,group_name):
        for num  in self.list().json()['tag_group']:
            if group_name in num['group_name']:
                return num['group_id']
        print('group_name not in num ')
        raise ValueError('group_name  not in num ')

    def bef_add(self,group_name,tag):
        if self.add(group_name,tag).json()['errcode'] == 40071:
            group_id = self.is_tag_group_name_exist(group_name)
            if not group_id:
                self.add(group_name,tag)
            else:
                self.delect_group_id(group_id)
                self.add(group_name,tag)
            return self.is_tag_group_name_exist(group_name)
