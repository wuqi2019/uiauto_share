from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Test_translate():
    def test_translateSearch(self):
        # 打开谷歌浏览器
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)

        # 访问百度首页
        driver.get('https://www.baidu.com/')

        # 悬停【更多】点击【查看百度产品】
        ele = driver.find_element_by_name("tj_briicon")
        ActionChains(driver).move_to_element(ele).perform()
        time.sleep(0.3)
        driver.find_element_by_name("tj_more").click()

        # 进入新标签页
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        time.sleep(0.5)

        # 点击【百度翻译】
        driver.find_element_by_link_text("百度翻译").click()

        # 进入新标签页
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        time.sleep(0.5)

        # 关闭弹窗
        ele = driver.find_element_by_css_selector(".desktop-guide-close")
        if ele:  # 若存在弹窗
            ele.click()

        # 输入要翻译的内容
        driver.find_element_by_id('baidu_translate_input').send_keys("交通")
        time.sleep(0.7)

        # 获取翻译内容
        ele = driver.find_element_by_css_selector('.ordinary-output.target-output.clearfix span')
        print("英语翻译为：", ele.text)

        # 断言 (期望)
        assert ele.text != ""

        time.sleep(2)
        driver.quit()