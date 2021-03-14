def qianghua(func):
    '''
    装饰器方法，需要加强哪个函数就把函数传到func里
    instance = self
    :param func:
    :return:
    '''
    def combination(*args, **kwargs):
        from appium_demo.page.basepage import BasePage
        instance: BasePage = args[0]
        try:
            res = func(*args, **kwargs)
            instance.error_num = 0 
            return res 
        except Exception as e:
            if instance.error_num < instance.max_num:
                instance.error_num += 1
                for ele in instance.black_list:
                    res = instance.driver.find_elements(*ele)
                    if len(res) > 0:
                        res[0].click()
                        return combination(*args, **kwargs)
            else:
                raise e
    return combination