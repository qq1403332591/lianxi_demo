import yaml
from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium_demo.page.reinforce import qianghua


class BasePage:
    black_list = [('id', 'iv_close')]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
            desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.release
            desired_caps['deviceName'] = 'V1938T'  # 手机/模拟器的型号：adb shell getprop ro.product.model
            desired_caps['appPackage'] = 'com.xueqiu.android'  # app的名字：adb shell dumpsys package XXX
            desired_caps[
                'appActivity'] = '.view.WelcomeActivityAlias'  # 同上↑  # .pages.splash.SplashActivity   pages.main.MainActivity
            desired_caps['noReset'] = True  # 使用app的缓存
            # desired_caps['skipDeviceInitialization'] = True  # 跳过设备初始化
            # desired_caps['autoLaunch'] = False # 直接使用打开的app进行测试
            # desired_caps['settings[settingsKey]'] = 0  # 动态元素查找的最大等待时间
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    @qianghua
    def find(self, by, locator=None):
        if locator is None:
            res: WebElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*by))
        else:
            res: WebElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by, locator))
        return res

    def open_yaml(self, path, func_name):
        with open(path, encoding='utf-8') as f:
            yaml_data = yaml.load(f)
        data_list = yaml_data[func_name]
        self.parsing_yaml(data_list)

    def parsing_yaml(self, data_list):
        for ele in data_list:
            if ele['action'] == 'click':
                self.find(ele['by'], ele['locator']).click()
            elif ele['action'] == 'send':
                self.find(['by'], ele['locator']).send_keys(ele['send_value'])
