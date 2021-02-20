import  pytest


@pytest.fixture()
def test_login():
    print("this is login func")
    return ("msg","successful")

@pytest.fixture()
def test_exit():
    print("this is quit func")
    return ("msg","已注销")


def test_case1(test_login,test_exit):
    print("test_case1这个方法需要登录")

def test_cast2():
    print("这个方法不需要登录")


def test_case3(test_login,test_exit):
    print("test_case3这个方法需要登录")




