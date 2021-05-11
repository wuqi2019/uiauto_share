from selenium.webdriver.common.by import By
from PO模式.pages.basePage import BasePage
from PO模式.utils.mySettings import URL
import time

class SsoHome(BasePage):
    def __init__(self,path='/home'):
        """
        SSO首页
        """
        super().__init__()      # 先执行父类的__init__方法
        self.path = URL+path

        # 以下封装页面元素寻找方法
        self.one_locator = (By.CSS_SELECTOR,".OnlyAppIcon_container__2wWSw > div:nth-child(1)")   # 企业安全中心
        self.two_locator = (By.CSS_SELECTOR, ".OnlyAppIcon_container__2wWSw > div:nth-child(2)")   # 综合监测中心
        self.three_locator = (By.CSS_SELECTOR, ".OnlyAppIcon_container__2wWSw > div:nth-child(3)")  # 数据分析中心

    # 企业安全中心
    def one_box(self):
        return self.get_element(self.one_locator)

    # 综合监测中心
    def two_box(self):
        return self.get_element(self.two_locator)

    # 数据分析中心
    def three_box(self):
        return self.get_element(self.three_locator)


    def to_page(self):
        """
        访问此页面的网址 SSO首页
        :return:
        """
        time.sleep(2)
        self.driver.get(self.path)

class SsoHomePageAction(SsoHome):    # 可以写一些页面中基本的操作
    pass

# 创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
sso_homeObj = SsoHomePageAction()

if __name__ == '__main__':
    sso_homeObj.to_page()
