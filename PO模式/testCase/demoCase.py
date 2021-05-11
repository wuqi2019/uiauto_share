from PO模式.pages.ssoHomePage import sso_homeObj
from PO模式.pages.riskDataAnalysisPage import RiskDataAnalysisActionObj
import time,requests

def test_project():
    # sso_homeObj.to_page()                     # 进入——SSO首页
    RiskDataAnalysisActionObj.to_page()         # 进入——营运车风险分析页

test_project()

