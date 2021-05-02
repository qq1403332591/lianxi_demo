import  pytest
'''
使用命令行运行 pytest 用例的时候，看不到 fixture 的执行过程.
如果我们想知道fixture的执行过程和先后顺序，可以加上 --setup-show 命令行参数，帮助查看 fixture 的执行过程.
'''


@pytest.fixture
def test_login():
    print("前置操作：准备数据this is login func")
    yield
    print("后置操作：清理数据")

@pytest.fixture
def test_exit():
    print("this is quit func")
    return ("msg","已注销")


def test_case1(test_login):
    '''
    先用运行test_login里面的办法，类似于setep_up，如果test_login中有yield会像teardown一样最后运行
    '''
    print("test_case1这个方法需要登录")

def test_cast2():
    print("这个方法不需要登录")


def test_case3(test_login,test_exit):
    print("test_case3这个方法需要登录")




