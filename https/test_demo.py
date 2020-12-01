import requests
import chevron
from jsonpath import jsonpath
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
        r = requests.get(url=url,headers=headre_data)
        print(r.request.headers)

    def test_auth(self):
        # 认证体系
        r = requests.get('https://httpbin.testing-studio.com/basic-auth/banana/123',
                         auth=HTTPBasicAuth("banana","123"))
        print(r.text)