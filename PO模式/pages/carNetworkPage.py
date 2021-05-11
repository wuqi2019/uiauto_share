from selenium.webdriver.common.keys import Keys
from PO模式.pages.basePage import BasePage
from PO模式.utils.mySettings import url
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class CarNetwork(BasePage):
    def __init__(self,
                 path="/dataScreen/carNetworkMonitoring?name=%25E8%25BD%25A6%25E8%25BE%2586%25E5%25AE%259E%25E6%2597%25B6%25E7%258A%25B6%25E6%2580%2581%25E7%259B%2591%25E6%25B5%258B"):
        """
        风险数据分析页，页面类
        :param path:
        """
        BasePage.__init__()  # 先执行父类的__init__方法
        self.path = url + path

        # 匹配所有市级卡片
        self.citycard_location = (By.CSS_SELECTOR, "div.amap-markers .Map_group__3Da77 div")

        # 车辆图标
        self.car_icon_location = (By.CSS_SELECTOR, ".InfoPanel_vehicle__3T18e.InfoPanel_low__16fjy >img")

        # 地图
        self.map_location = (By.CSS_SELECTOR, ".amap-labels")

        # 车辆卡片的详情 风险分析
        self.carinfo_location = (By.CSS_SELECTOR, ".InfoPanel_btns__2hak4 >a:nth-child(2)")
        self.carriskinfo_location = (By.CSS_SELECTOR, ".InfoPanel_btns__2hak4 >a:nth-child(2) > ul >li:nth-child(2)")

    def to_page(self):
        """
        访问此页面的网址 SSO首页
        :return:
        """
        time.sleep(3)
        self.driver.get(self.path)

    def cityNameboxes(self):
        return self.driver.find_element(*self.citycard_location)  # 这里不能用显示等待

    def carIconBoxes(self):
        return self.driver.find_elements(*self.car_icon_location)  # 这里不能用显示等待

    def allMap(self):
        return self.driver.find_element(*self.map_location)

    def carinfoboxes(self):
        return self.driver.find_element(*self.carinfo_location)

    def riskinfobox(self):
        return self.driver.find_element(*self.carriskinfo_location)


class CarNetworkAction(CarNetwork):
    pass


# 创建对象类实例, 其他模块引用此对象, 可保持对象在内存中只有一个
CarNetworkActionOpj = CarNetworkAction()

if __name__ == '__main__':
    CarNetworkActionOpj.to_page()
