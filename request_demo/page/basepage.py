import json

import requests


class BasePage():
    params = {}

    def __init__(self):
        self.token = self.get_token()
        self.params = {}

    def get_token(self):
        data = {"method": "get",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                "params": {'corpid': "wwafa879921b0e5a41", 'corpsecret': "-Pvw3PqU_ylhpj75VroMnqOfRW5pXJfsLguXMuqemQg"}
                }
        r = self.send(data)
        # print(json.dumps(r.json(), indent=2))
        return r.json()['access_token']

    def send(self, kwargs):
        raw_data = json.dumps(kwargs)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        kwargs = json.loads(raw_data)
        r = requests.request(**kwargs)
        return r
