from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from constant import *

import time

browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

browser.get(constant.test_deploy_login_url)

name = browser.find_element_by_id("loginform-username")
pwd = browser.find_element_by_id("loginform-password")
print("登录deploy")
name.clear()
pwd.clear()
name.send_keys(constant.lyw)
pwd.send_keys(constant.lyw_pwd)
browser.find_element_by_name("login-button").click()
## 测试环境构建
for project_name in constant.build_projects:
    browser.get(constant.test_deploy_task_url+constant.project_of_id.get(project_name))
    time.sleep(5)
    browser.find_element_by_class_name("btn-primary").click()
    time.sleep(0.5)
    browser.find_element_by_link_text('上线').click()
    time.sleep(0.5)
    browser.find_element_by_class_name("btn-deploy").click()
    print(project_name+"正在发布上线")
    time.sleep(1)











