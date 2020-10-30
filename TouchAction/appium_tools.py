from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, locator):
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout=10).until(lambda x: x.find_element(*locator))


def find_by_scroll(driver, text_value):
    '''
    滚动查找元素的方法
    :param driver:需要传入的driver
    :param text_value:文本值
    :return:
    '''
    return driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                               'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{}").instance(0));'.format(
                                   text_value))
