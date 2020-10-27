import pytest
import allure

@allure.title("测试登录成功")
def test_biaoti():
    print("hahah")

def test_html():
    allure.attach("<head></head><body>首页</body>","这是错误页的结果信息",allure.attachment_type.HTML)

def test_tupian():
    allure.attach.file("2.JPG",name="这是一个图片",attachment_type=allure.attachment_type.JPG)

def test_vedio():
    allure.attach.file("6b756ff660ca186e4776b3bdc012715a.mp4",name="这是一个视频",
                  attachment_type=allure.attachment_type.MP4)