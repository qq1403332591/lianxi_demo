from appium import  webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_click():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
        desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.release
        desired_caps['deviceName'] = 'V1938T'  # 手机/模拟器的型号：adb shell getprop ro.product.model
        desired_caps['appPackage'] = 'io.appium.android.apis'  # app的名字：adb shell dumpsys package XXX
        desired_caps['appActivity'] = '.view.PopupMenu1'  # 同上↑  # .pages.splash.SplashActivity   pages.main.MainActivity
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['unicodeKeyboard'] = True  # 为了支持中文
        desired_caps['resetKeyboard'] = True  # 设置成appium自带的键盘
        desired_caps['noReset'] = True  # 使用app的缓存
        desired_caps['skipDeviceInitialization'] = True   # 跳过设备初始化
        desired_caps['autoLaunch'] = False # 直接使用打开的app进行测试
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.TextView"][@text="Search"]').click()
        print(self.driver.page_source)
        assert  "Clicked popup menu item Search" in self.driver.page_source

