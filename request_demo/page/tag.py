import json

import requests


class Page_Tag():
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': "wwafa879921b0e5a41",
                                 'corpsecret': "-Pvw3PqU_ylhpj75VroMnqOfRW5pXJfsLguXMuqemQg"})

        # print(json.dumps(r.json(), indent=2))
        return r.json()['access_token']

    def get_enterprise_label(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
                          json={'tag_id': []}, params={"access_token": self.token})
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

    def before_del(self, tag_ids):
        tagid = []
        r = self.delect_tag(tag_ids)
        if r.json()['errcode'] == 40068:
            for items in tag_ids:
                if not self.is_find_tag_id_exist(items):
                    for nums in self.add_tag('yydsddd',id=items).json()['tag_group']:
                            if 'yyd' in nums['name']:
                                tagid.append(num['id'])
                                self.delect_tag(tagid)







