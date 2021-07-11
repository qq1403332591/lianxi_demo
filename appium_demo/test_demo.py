from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Testcase():
    def setup(self):
        """
            获取设备driver
        """
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
        desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.release
        desired_caps['deviceName'] = 'vivo x6plus d'  # 手机/模拟器的型号：adb shell getprop ro.product.model
        desired_caps['appPackage'] = 'com.taobao.idlefish'  # app的名字：
        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
        desired_caps['appActivity'] = 'com.taobao.fleamarket.home.activity.MainActivity'  # 同上↑
        desired_caps['noReset'] = True
        #desired_caps['autoLaunch'] = False
        # 去打开app，并且返回当前app的操作对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def test_case01(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'通讯录')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'添加成员')]").click()
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys('123')
        self.driver.find_element_by_id("fwi").send_keys('13153117138')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)\
                                 .instance(0)).scrollIntoView(new UiSelector().text("保存").instance(0));').click()
        self.driver.back()
