import pytest
import yaml
from testkuangjia.chufa import Jisuanqi


def get_datas():
    with open("./datas.yaml") as f:
        datas = yaml.load(f)
        add_datas = datas['add']['datas']
        add_ids = datas['add']["ids"]
        print(add_datas)
        print(add_ids)
        return [add_datas,add_ids]





class TestCase():
    @pytest.mark.parametrize("a,b,c",get_datas()[0] ,ids= get_datas()[1])
    def test_chufa(self, a, b, c):
        self.jsq = Jisuanqi()
        res = self.jsq.chufa(a, b)
        assert res == c



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

