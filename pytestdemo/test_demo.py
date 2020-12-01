from pytestdemo.jisuanqi import jisuanqi
import pytest

class TestCase:
    def setup_class(self):
        self.jsq = jisuanqi()


    @pytest.mark.parametrize('a,b,c',([1,1,1],[6,2,3],[0,1,0]),ids=['haha','wawa'])
    def test_jiafa(self,a,b,c):
        result = self.jsq.jiafa(a,b,c)
        assert c == result


    def test_jianfa(self):
        datalist = [[3,2,1],[5,3,2],[6,3,3]]
        for num in range(0,len(datalist)):
            print(datalist[num])
            # print(num[1])
            # print(datalist[num][0])
            # res = self.jsq.jianfa(datalist[num][0],datalist[num][1])
            # assert res == datalist[num][2]



