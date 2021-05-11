import time
from selenium.webdriver.common.by import By
from PO模式.pages.basePage import BasePage
from PO模式.utils.mySettings import url

class RiskDataAnalysis(BasePage):
    def __init__(self,path="/overview/riskDataAnalysis"):
        """
        风险数据分析页，页面类
        :param path:
        """
        super().__init__()    # 先执行父类的__init__方法
        self.path = url+path

        # 以下封装页面元素寻找方法
        # 筛选条件_风险点名称
        self.riskName_locator = (By.ID,"riskName")
        # 搜索按钮
        self.search_button_locator = (By.CSS_SELECTOR,'button[type="submit"]')
        #风险卡片文字
        self.riskNameText_locator =(By.CSS_SELECTOR,".ant-descriptions-title")



    # 定位
    def to_page(self):
        """
        访问此页面的网址 SSO首页
        :return:
        """
        time.sleep(3)
        self.driver.get(self.path)

    def riskName_input_box(self):
        return self.get_element(self.riskName_locator)

    def search_button_box(self):
        return self.get_element(self.search_button_locator)

    def list_of_riskName_boxes(self):
        """匹配列表当中的每一个项目名称, 返回元素列表"""
        return self.get_elements(self.riskNameText_locator)




class RiskDataAnalysisAction(RiskDataAnalysis):
    pass

# 创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
RiskDataAnalysisActionObj = RiskDataAnalysisAction()

if __name__ == '__main__':
    RiskDataAnalysisActionObj.to_page()
    time.sleep(3)

