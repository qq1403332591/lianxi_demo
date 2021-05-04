import pytest


class Test(object):
    '''
    断言1失败会执行后续代码及断言2
    '''
    def test_01(self):
        """用例1"""
        print('执行test_01断言1')
        pytest.assume(0 == 1)
        pytest
        print('执行test_01断言2')
        pytest.assume(1 == 2)

    def test_02(self):
        """用例2"""
        print('执行test_02断言1')
        pytest.assume(3 == 3)
        print('执行test_02断言2')
        pytest.assume(4 == 4)