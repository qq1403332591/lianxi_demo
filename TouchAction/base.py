from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_case():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
        desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.release
        desired_caps['deviceName'] = 'V1938T'  # 手机/模拟器的型号：adb shell getprop ro.product.model
        desired_caps['appPackage'] = 'com.znb.zxx'  # app的名字：adb shell dumpsys package XXX
        desired_caps[
            'appActivity'] = '.pages.splash.SplashActivity'  # 同上↑  # .pages.splash.SplashActivity   pages.main.MainActivity
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['unicodeKeyboard'] = True  # 为了支持中文
        desired_caps['resetKeyboard'] = True  # 设置成appium自带的键盘
        desired_caps['noReset'] = True  # 使用app的缓存
        desired_caps['skipDeviceInitialization'] = True   # 跳过设备初始化
        desired_caps['dontStopAppOnReset'] = True # 直接使用打开的app进行测试

        # 去打开app，并且返回当前app的操作对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def test_touchaction(self):
        self.driver.find_element_by_id('splash_jumpOver_btn').click()
        action = TouchAction(self.driver)
        window = self.driver.get_window_size()  # 获取设备的分辨率
        width = window["width"]
        height = window["height"]
        x1 = int(width*0.5)
        y_start = int(height*0.8)
        y_end = int(height*0.2)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()
        '''
        pree(x=xxx,y=xxx) 传入起始滑动的x,y的坐标
        move_to(x=xxx,y=xxx) 要滑到到哪个地方的x,y坐标
        release()结束动作
        perform()执行操作
        '''

    def teardown(self):
        self.driver.quit()