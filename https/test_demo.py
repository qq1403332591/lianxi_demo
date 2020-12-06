import json
import requests
from requests.auth import HTTPBasicAuth


class TestHttp:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)

    def test_query(self):
        query_data = {
            "level": 1,
            "name": "yaoyingdong"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=query_data)
        print(r.text)
        assert r.status_code == 200

    def test_login(self):
        data = 'params={"mobile","xxx","password","a123456","orgin":"1"}'
        r = requests.post("xxxxxx", data=data, verify=False)
        print(r.text)

    def test_login1(self):  # 登录
        url = 'xxxxx'
        data = {"params":
                    '{"mobile": "xxx", "password": "a123456", "origin": "1"}'
                }
        res = requests.post(url=url, json=data,verify=False)
        print(res.json())

    def test_hogwart_json(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(jsonpath(r.json(), '$..name'))

    def test_cookie(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        headre_data = {"Cookie":"dabcasd",
                       "User-Agent":"hogwarts"
                       }
        # cookie_data = {"Cooike":"hogwarts",
        #                "Uer-Agent":"school"}
        r = requests.get(url=url, headers=headre_data)
        print(r.request.headers)

    def test_auth(self):
        # 认证体系
        r = requests.get('https://httpbin.testing-studio.com/basic-auth/banana/123',
                         auth=HTTPBasicAuth("banana", "123"))
        print(r.text)

    def test_demo(self):
        with open("data.txt", encoding="utf-8") as f:
            duser_dict = json.dumps(f.read())
            user_dict = json.loads(duser_dict)
            print(user_dict)

    def test_demo01(self):
        list_1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        i_num = [i for i in list_1 if i > 4 if i > 80]
        print(i_num)
