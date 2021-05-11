from selenium import webdriver
import time

# 打开谷歌浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(30)

# 访问百度首页
driver.get('https://www.baidu.com/')

# 输入搜索内容
driver.find_element_by_id('kw').send_keys("海康交通大数据")
time.sleep(0.5)

# 点击【百度一下】
driver.find_element_by_id('su').click()
time.sleep(0.5)


# 断言 ---- 能否搜索到输入内容(海康交通大数据)
# 获取标题或内容的搜索关键词（红色的）
result = driver.find_elements_by_css_selector("#container #content_left a em")
for one in result:
    if  "海康交通大数据" in one.text:
        assert "海康交通大数据" in one.text
        break                                   # 存在 一个就断言成功


