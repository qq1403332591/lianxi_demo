import pytest

from pytestdemo.jisuanqi import jisuanqi


@pytest.fixture(autouse=False)
def test_login():
    # setup 操作
    print("前置操作：准备数据this is login func")
    # return 操作
    yield ['yaoyingdong','123']
    # teardown操作
    print("后置操作：清理数据")

@pytest.fixture
def test_exit():
    print("this is quit func")
    return ("msg","已注销")


@pytest.fixture()
def jiafa(a,b):
    c = a + b
    return c


@pytest.fixture(scope='class')
def get_calc():
    '''
    使用fixture + conftest文件完成setup_class的动作
    '''
    print('计算开始')
    jsq = jisuanqi()
    yield jsq
    print('计算结束')
