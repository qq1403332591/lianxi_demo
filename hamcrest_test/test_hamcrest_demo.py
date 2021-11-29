
import requests
from hamcrest import *
from jsonpath import jsonpath


def test_01():
    a = "123"
    assert_that(a, equal_to("123"))  #  断言变量a 是不是等于后面那个对象


def test_hamcrest_02():
    proxy = {
        "http":"http://127.0.0.1:8888",
        "https":"http://127.0.0.1:8888"
    }
    r =requests.get('https://home.testing-studio.com/categories.json',proxies=proxy,verify=False)
    print(r.json())
    assert r.status_code == 200
    # print(jsonpath(r.json(),'$..name'))s
    eles = r.json()['category_list']['categories']
    for ele in range(len(eles)):
        print(eles[ele]['name'])

    print(jsonpath(r.json(), '$..name'))


