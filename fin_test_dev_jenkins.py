from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from constant import *

browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

browser.get(constant.test_dev_jenkins_login_url)
print("test build start ......")
name = browser.find_element_by_id("j_username")
pwd = browser.find_element_by_name("j_password")
name.clear()
pwd.clear()
name.send_keys(constant.user_name)
pwd.send_keys(constant.user_pwd)
browser.find_element_by_id("yui-gen1-button").click()
time.sleep(1)
## 测试环境构建
for project_name in constant.build_projects:
    search = browser.find_element_by_id("search-box")
    search.clear()
    search.send_keys(project_name + Keys.RETURN)
    print(project_name+">>>> test build end ......")
    time.sleep(2)
    browser.find_element_by_link_text("立即构建").click()

print("test build end ......")

def test_jenkins_build(browser):
    browser.get(constant.test_dev_jenkins_login_url)
    print("test build start ......")
    name = browser.find_element_by_id("j_username")
    pwd = browser.find_element_by_name("j_password")
    name.clear()
    pwd.clear()
    name.send_keys(constant.user_name)
    pwd.send_keys(constant.user_pwd)
    browser.find_element_by_id("yui-gen1-button").click()
    time.sleep(1)
    ## 测试环境构建
    for project_name in constant.build_projects:
        search = browser.find_element_by_id("search-box")
        search.clear()
        search.send_keys(project_name + Keys.RETURN)
        print(project_name+">>>> test build end ......")
        time.sleep(2)
        browser.find_element_by_link_text("立即构建").click()











