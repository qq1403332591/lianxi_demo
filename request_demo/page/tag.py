import json

import requests
import yaml

from request_demo.page.basepage import BasePage


class Page_Tag(BasePage):

    def get_enterprise_label(self):
        # r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        #                   json={'tag_id': []}, params={"access_token": self.token})
        # print(json.dumps(r.json(), indent=2))
        # return r

        with open("../page/api_data.yaml", encoding="utf-8") as f:
            data = yaml.load(f)
        self.params = self.params
        self.params["token"] = self.token
        r = self.send(data['get_list'])
        print(json.dumps(r.json(), indent=2))
        return r

    def exit_tag(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag', json={
            "id": "etXT2CDwAArKWHeDCmTXgSfXfYDqDCiw",
            "name": "NEW_TAG_NAME",
        }, params={'access_token': self.token})
        # print(json.dumps(r.json(), indent=2))
        return r

    def add_tag(self, tag_name1):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json={
                              "group_name": "GROUP_NAME",
                              "tag": tag_name1
                          })
        print(json.dumps(r.json(), indent=2))
        return r

    def delect_tag(self, tag_id, **kwargs):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={'access_token': self.token},
                          json={
                              "tag_id":
                                  tag_id,
                              **kwargs
                          })
        print(json.dumps(r.json(), indent=2))
        return r

    def find_tag_id_is_not_exist(self, tag_name1):
        '''
        查找tagname是否存在
        '''
        if self.add_tag(tag_name1).json()['errcode'] == 40071:
            tag_name1_id = self.find_tag_id(tag_name1)
            if not tag_name1_id:
                return False
            self.delect_tag(tag_name1_id)
            self.add_tag(tag_name1)
            return True
        self.add_tag(tag_name1)
        return True

    def find_tag_id(self, tag_name1):
        '''
        根据tag_name 查找id
        '''
        for tag_group in self.get_enterprise_label().json()['tag_group']:
            for tag in tag_group['tag']:
                if tag_name1 == tag['name']:
                    return tag['id']
        print('tag_name not in list')
        return False

    def is_find_tag_id_exist(self, tag_id):
        '''
        根据tag_name 查找id
        '''
        for tag_group in self.get_enterprise_label().json()['tag_group']:
            for num in tag_group['tag']:
                if tag_id in num['id']:
                    return True
        print('tag_id not in list')
        return False

    def open_yaml(self, key_name):
        with open("../page/api_data.yaml", encoding="utf-8") as f:
            datas = yaml.load(f)
            r = self.params_data(datas[key_name])
            return r

    def params_data(self, ultimately_key):
        for data in ultimately_key:
            if "select" == data["action"]:
                return data['sql']


