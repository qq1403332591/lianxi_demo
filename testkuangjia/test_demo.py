import pytest
import yaml
from testkuangjia.chufa import Jisuanqi


def get_datas(path,key):
    with open(path) as f:
        datas = yaml.load(f)
        add_datas = datas[key]['datas']
        add_ids = datas[key]["ids"]
        return [add_datas,add_ids]





class TestCase():
    #  @pytest.mark.parametrize("a,b,c",get_datas()[0] ,ids= get_datas()[1])
    # def test_chufa(self, a, b, c):
    #     self.jsq = Jisuanqi()
    #     res = self.jsq.chufa(a, b)
    #     assert res == c



    @pytest.mark.parametrize("a,b,c", [
        [0.1, 0.1, 0.2]
    ])
    def test_float(self, a, b, c):
        self.jsq = Jisuanqi()
        res = self.jsq.jiafa(a,b)
        assert round(res,1) == c

    @pytest.mark.parametrize("a,b,c", [
        [0.1, 0, 0.2],[2,0,2],[21,0,True]
    ])
    def test_zero(self,a,b,c):
        with pytest.raises(ZeroDivisionError):
            self.jsq = Jisuanqi()
            res = self.jsq.chufa(a,b)

    @pytest.mark.parametrize("a,b", get_datas('./datas.yaml', 'chufa')[0], ids=get_datas('./datas.yaml', 'chufa')[1])
    def test_chufa(self, a, b):
        jisuan = Jisuanqi()
        c = jisuan.chufa(a, b)
        print(c)
        # print(get_datas('./datas.yaml', 'chufa')[0])
        # print(get_datas('./datas.yaml', 'chufa')[1])


