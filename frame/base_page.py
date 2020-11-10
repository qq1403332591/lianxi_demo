import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame.black_list import handle_black


class BasePage():
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0
    def __init__(self, driver: WebDriver = None):
        """
        初始化应用
        """
        if driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
            desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.release
            desired_caps['deviceName'] = 'V1938T'  # 手机/模拟器的型号：adb shell getprop ro.product.model
            desired_caps['appPackage'] = 'com.xueqiu.android'  # app的名字：adb shell dumpsys package XXX
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'  # 同上↑  # .pages.splash.SplashActivity   pages.main.MainActivity

            desired_caps['resetKeyboard'] = True  # 设置成appium自带的键盘
            desired_caps['noReset'] = True  # 使用app的缓存
            desired_caps['skipDeviceInitialization'] = True  # 跳过设备初始化
            #desired_caps['autoLaunch'] = False # 直接使用打开的app进行测试
            # desired_caps['settings[settingsKey]'] = 0  # 动态元素查找的最大等待时间
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """
        if locator is None:
            # 如果传的元素是一个，只有 by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素是二个，既有 by ，又有 locator
            result = self.driver.find_element(by, locator)
        return result

    def open_yaml(self,file,key_name):
        # 读取yaml，取出关键数据，用parse解析
        with open(file,encoding="utf-8") as f:
            data = yaml.load(f)
            self.parse(data[key_name])


    def parse(self,func):
        # 遍历每一个步骤
        for ele in func:
            # 如果操作是click就去点击
            if "click" == ele["action"]:  # 当action是click的时候
                self.find(ele["by"],ele["locator"]).click()   # 去查找他的元素并且点击
            elif "send" == ele["action"]:
                self.find(ele["by"],ele["locator"]).send_keys(ele["content"])
