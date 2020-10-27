查看allure的使用帮助文档：pytest --help | findstr allure

pytest test_allure.py  --allure-features="登录功能" -vs
这个是单独运行@allure.feature标题是登录功能的所有用例
-vs：查看详细日志


pytest test_allure.py  --allure-stories="测试成功的场景" -vs
单独运行@allure.story的用例，allure.story可以理解成用例的不同场景


--allure-stories --allure-features 也可以同时使用，优先执行前面的
