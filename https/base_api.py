import json

import requests


class Base_Api():
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpsecret = '-Pvw3PqU_ylhpj75VroMnqOfRW5pXJfsLguXMuqemQg'
        corpid = "wwafa879921b0e5a41"
        body = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{"corpid": corpid, "corpsecret": corpsecret}
               }
        r = self.send(body)
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r
