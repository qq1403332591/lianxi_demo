from appium.webdriver.common.mobileby import MobileBy

from TouchAction.appium_tools import Base, find_element


class Test_Attribute(Base):
    def test_attribute(self):
        el1 = self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"设置")]')
        print(el1.get_attribute("class"))  # 获取元素的class属性的值
