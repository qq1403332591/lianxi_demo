import pytest
import yaml

from pytestdemo.jisuanqi import jisuanqi


def open_yaml():
    '''
    解析测试数据
    '''
    with open('../pytestdemo/datas.yaml') as f:
        datas = yaml.load(f)
    add_datas = datas['add']['datas']
    ids_datas = datas['add']['ids']
    return [add_datas, ids_datas]

def open_step(open_step_file,num1,num2,num3):

    with open(open_step_file) as f:
        datas = yaml.load(f)
    for step in datas:
        if step == "jiafa":
            result = jisuanqi().jiafa(num1,num2)
        elif step == "add1":
            result = jisuanqi().jiafa1(num1,num2)
        elif step == "add2":
            result = jisuanqi().jiafa2(num1,num2)
        assert num3 == result








class Test_Case1:
    def jiafa(self,a,b):
        c = a + b
        return c
    def test_case1(self):
        case_data = [[111,222,333],[222,333,555],[455,666,1121]]
        for i in range(0,len(case_data)):
            c = self.jiafa(case_data[i][0],case_data[i][1])
            assert c == case_data[i][2]


    @pytest.mark.parametrize("a",[111,222,333])
    @pytest.mark.parametrize("b",[222,333,444])
    def test_case2(self,a,b):
        print(a,b)



    @pytest.mark.parametrize("a,b,c",open_yaml()[0],ids=open_yaml()[1])
    def test_case3(self,a,b,c):
        # print(open_yaml()[0])
        # print(open_yaml()[1])
        c = a + b
        print(c)

    def test_case4(self):
        open_step("../pytestdemo/step_data.yaml", 1, 2,3)


    @pytest.fixture()
    def test_login(self):
        print('开始登陆')
        yield ['my name is yaoyingdong']
        print('登出操作')



    def test_case5(self,test_login):
        a = test_login
        print(a)
        print('case5开始')


    def test_case6(self,get_calc):
        get_calc.jiafa(1,2)