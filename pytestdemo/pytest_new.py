import pytest
import yaml


def open_yaml():
    with open('../pytestdemo/datas.yaml') as f:
        datas = yaml.load(f)
    add_datas = datas['add']['datas']
    ids_datas = datas['add']['ids']
    return [add_datas, ids_datas]



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



