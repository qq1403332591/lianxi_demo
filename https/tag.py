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

    def add(self, group_name, tag, **kwargs):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json=
                          {
                              "group_name": group_name,
                              "tag": tag, **kwargs
                          }
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
        #print(json.dumps(r.json(), indent=2))  # 将python对象编码成Json字符串
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
        return r

    def before_delect(self, group_ids):
        delect_group_ids = []
        r = self.delect_group_id(group_ids)
        if r.json()['errcode'] == 40068:
            # 如果标签不存在，就添加一个标签，将他的group_id 存储进来
            for group_id in group_ids:
                if not self.find_group_id_by_id(group_id):
                    group_id = self.bef_add("TMP1234",[{"name":"tag_test1"}])
                    delect_group_ids.append(group_id)
                # 如果标签存在，就将他存入标签组
                else:
                    delect_group_ids.append(group_id)
                r = self.delect_group_id(delect_group_ids)
        return r


    def find_group_id_by_name(self, group_name):
        # 查询元素是否存在，如果不存在，报错
        for num in self.list().json()['tag_group']:
            if group_name in num['group_name']:
                return num['group_id']
        print('group_name not in num ')
        return ""

    def find_group_id_by_id(self, group_id):
        # 查询元素是否存在，如果不存在，报错
        for num in self.list().json()['tag_group']:
            if group_id in num['group_id']:
                return True
        print('group_id not in num ')
        return False

    def bef_add(self, group_name,tag):
        if self.add(group_name,tag).json()['errcode'] == 40071:
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                # 元素不存在 但是返回了40071说明接口有问题了
                return False
            else:
                self.delect_group_id(group_id)
                self.add(group_name,tag)
        res = self.find_group_id_by_name(group_name)
        return res
