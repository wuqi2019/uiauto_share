from PO模式.utils.mySettings import URL,implicitly_wait_time,usernanme,password
from selenium import webdriver
import requests,time

class Driver:
    """浏览器驱动工具 类"""
    _driver = None
    @classmethod            # (类方法，不用实例化就可以调用嗷)
    def get_driver(cls,rowebr_name="Chrome"):
        """
        获取浏览器驱动对象
        :param brower_name:
        :return:
        """
        # 如果空 才创建
        if cls._driver is  None:
            if brower_name == "Chrome":
                cls._driver =webdriver.Chrome()
            elif brower_name == "Firefox":
                cls._driver = webdriver.Firefox()
            # 最大化窗口
            cls._driver.maximize_window()
            # 访问默认网页
            cls._driver.get("{URL}/login")
            cls._driver.implicitly_wait(implicitly_wait_time)

            # 执行登录
            cls._login()            # 类调  类方法
        return cls._driver

    @classmethod
    def _login(cls):
        """
        私有方法，只能在类里边使用
        类外部无法使用，子类不能继承
        只在浏览器刚打开的时候登陆一次
        :return:
        """
        cls._driver.find_element_by_id("normal_login_loginName").send_keys(usernanme)
        cls._driver.find_element_by_id("normal_login_password").send_keys(password)
        cls._driver.find_element_by_css_selector(".ant-btn.Login_button__1rd4Y.ant-btn-primary").click()
        # 登录成功后先进入营运车，把token传给浏览器
        cls._driver.find_element_by_css_selector(".OnlyAppIcon_container__2wWSw > div:nth-child(1)").click()

if __name__ == '__main__':
    # 访问登录页，（最大窗口化），完成登录，并返回driver
    Driver().get_driver()




