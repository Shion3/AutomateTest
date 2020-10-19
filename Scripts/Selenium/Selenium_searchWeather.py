# 导入webdriver
from selenium import webdriver
# 引入WebDriverWait 用于执行等待某元素显示
from selenium.webdriver.support.wait import WebDriverWait
# 引入expected_conditions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time
# 使用Chrome
driver = webdriver.Chrome()
# 打开site
driver.get("https://www.bing.com")
# 停留3秒
time.sleep(3)
# 获取输入框
inputElement = driver.find_elements_by_class_name('b_searchbox')[0]
# 输入内容
inputElement.send_keys('天气预报')
# 获取提交按钮
submitElement = driver.find_elements_by_id('sb_form_go')[0]
submitElement.click()
# 等待结果页
wait = WebDriverWait(driver, 10, 0.5)
# b_content
element = wait.until(expected_conditions.presence_of_element_located(
    (By.ID, 'b_content')), message='aaa')
print(element.is_displayed())
# 滑动滚动条
driver.execute_script('window.scrollTo(0,10000)')
time.sleep(1)
driver.execute_script('window.scrollTo(0,0)')
time.sleep(1)
# 退出
driver.quit()
