import pytest
import yaml
class Testdemo():


    @pytest.mark.parametrize("var",yaml.safe_load(open("./data.yml")))
    def test_demo01(self,var):
        if "test" in var:
            print("这是一个测试环境，ip地址是",var["test"])

        elif "admin" in var:
            print("这是一个正式环境，正式环境的地址是{}".format(var["admin"]))


