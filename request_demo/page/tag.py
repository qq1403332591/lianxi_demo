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

    def get_Enterprise_label(self):
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

    def add_tag(self, tag_name1, tag_name2):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json={
                              "group_name": "GROUP_NAME",
                              "tag": [{
                                  "name": tag_name1,
                                  "order": 1
                              },
                                  {
                                      "name": tag_name2,
                                      "order": 2
                                  }
                              ]
                          })
        print(json.dumps(r.json(), indent=2))
        return r

    def delect_tag(self,TAG_ID_1,**kwargs):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                      params={'access_token': self.token},
                      json={
                          "tag_id": [
                              TAG_ID_1,
                              kwargs
                          ]
                      })
        print(json.dumps(r.json(), indent=2))
        return r
