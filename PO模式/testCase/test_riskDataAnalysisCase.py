import unittest,time,os,pytest,allure
from PO模式.pages.riskDataAnalysisPage import RiskDataAnalysisActionObj
#unittest.TestCase

@allure.feature("风险分析")
class TestRiskDataAnalysisCase():
    @allure.title("风险卡片搜索")
    @allure.description("""
    按风险名称搜索
    """)
    def test_card_search(self):
        RiskDataAnalysisActionObj.to_page()

        time.sleep(1)
        """1.选到筛选框风险点，输入名字并搜索"""
        name = "车道偏离"
        RiskDataAnalysisActionObj.riskName_input_box().send_keys(name)
        RiskDataAnalysisActionObj.search_button_box().click()
        time.sleep(2)

        """2.获取搜索出来的列表"""
        # 获取卡片列表
        riskName_list = RiskDataAnalysisActionObj.list_of_riskName_boxes()
        time.sleep(3)

        """3.断言验证，搜索出来的列表，名字都包含搜索的文本"""
        for riskName in riskName_list:
            assert name   in  riskName.text


if __name__ == '__main__':
    # unittest.main()
    for one in os.listdir('../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../report/tmp/{one}')
    pytest.main(['test_riskDataAnalysisCase.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure serve ../report/tmp')
