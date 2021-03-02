import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCase:
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222" # 终端运行Google\ Chrome --remote-debugging-port=9222
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_get_cookies(self):
        #  使用复用浏览器的方法获取到cookies，将cookies保存下来。
        cookies = self.driver.get_cookies()



    def test_case1(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for num in self.cookies:
            self.driver.add_cookie(num)  # 因为addcookie需要传入字典，我们拿到的cookies是一个列表。
        self.driver.refresh()  # 刷新网页
        time.sleep(5)

    def test_shelve(self): # 专门对数据进行数据化存储的库
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688854150762864'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ekWIJNvpe3l557YpAF6XpBL8j1ugIwGYKdbCa1DCKf-C4W2b5_9dBndA6tl61s6zQMEaW1CRkGkPTj63hd5eH82YCc_dpikBm1KYvIuKYw1Rbtvb1OJTNorfzv441pQU-PFpJ6tqt_cdzHReakCi6TPnvHgt7hU2qCouUMmhG1yAAVT7iyCtRu1bf8WvFrfalQ7AowFFHcF-DyARFqLwQLjy00BjnGvBnPtx7oSzukaPoHckqQCnejDoG6RCIejb5isfrRkDPPyC4I5LJJ1QFQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688854150762864'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325097168221'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'LL-88R6q0a3R0IdNYhCVgJqtCa7csD8m61-IP2ndiKNaub_Xk5FcD8e6K8OYLV5X'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7305391'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614634726, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '14h27nd'}, {'domain': '.qq.com', 'expiry': 1614690378, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.401177970.1614603192'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614603964'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '242178468936345'}, {'domain': '.qq.com', 'expiry': 1677675978, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.130095980.1614092144'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645628142, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1646139964, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614092144,1614603191,1614603964'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1492328210'}, {'domain': '.work.weixin.qq.com', 'expiry': 1617195981, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '9802d8c0300e3c4c11dcec117cb9fb89ae73a1dbbef5169770b036e0a3ab4bf2'}, {'domain': '.qq.com', 'expiry': 2147483642, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'h9jISkH+e0'}]
        db = shelve.open('cookies')
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for num in cookies:
            self.driver.add_cookie(num)

        self.driver.refresh()
        time.sleep(5)


    def teardown(self):
        self.driver.quit()


