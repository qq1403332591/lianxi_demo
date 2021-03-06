import pytest
import allure

@allure.feature("登录功能")  # feature相当于一个大的功能模块
class TestCase():
    allure.story("测试成功的场景")
    """
        story相当于对应这个功能或者模块下的不同场景，分支功能，
        属于大模块feature之下的结构，报告在features中显示,相当于testcase
    """
    @allure.step("步骤1")
    def test_case1(self):
        with allure.step("第一步：启动app"):  # 步骤细节，可以放在测试方法用例里面，但测试步骤的代码需要被该语句包含
            print("aaa")

        with allure.step("第二步:输入账号密码"):
            print('bbb')

        with allure.step("第三步：点击登录"):
            print("ccc")


    allure.story("测试失败的场景")
    @allure.step("步骤2")
    def test_case2(self):
        print("账号密码不对登录失败")

    allure.story("测试失败的场景")
    @allure.step("步骤3")
    def test_case3(self):
        print("密码为空登录失败")
