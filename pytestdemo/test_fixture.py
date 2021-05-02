import  pytest
'''
使用命令行运行 pytest 用例的时候，看不到 fixture 的执行过程.
如果我们想知道fixture的执行过程和先后顺序，可以加上 --setup-show 命令行参数，帮助查看 fixture 的执行过程.
'''


@pytest.fixture(autouse=True,scope=function)
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


# 传入装饰器方法的名字
def test_case1(test_login):
    '''
    先用运行test_login里面的办法，类似于setep_up，如果test_login中有yield会像teardown一样最后运行
    '''
    print("test_case1这个方法需要登录")


# 直接通过函数名字调用
@pytest.mark.usefixtures("test_login")
def test_cast2():
    print("test_case2这个方法需要登录")


# 如果测试用例里需要fixture的返回值的话，需要以参数的形式传入.
def test_case3(test_login):
    print(test_login)
    print("test_case3这个方法需要登录")

# 允许使用多个装饰器,运行顺序就是传入的顺序
def test_case4(test_login,test_exit):
    print(test_login)
    print(test_exit)
    print("test_case4运行成功")


# autouser的用法:如果fixture方法设置了True会自动每个办法传入fixture的方法.不需要手动去传
# scope：作用域
def test_case5():
    print("test_case5运行成功")
