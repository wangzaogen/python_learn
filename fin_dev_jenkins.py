from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from constant import *

import time

browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

browser.get(constant.dev_jenkins_login_url)

build_projects = constant.build_projects
project_branch = constant.project_branch

name = browser.find_element_by_id("j_username")
pwd = browser.find_element_by_name("j_password")
name.clear()
pwd.clear()
name.send_keys(constant.user_name)
pwd.send_keys(constant.user_pwd)
browser.find_element_by_id("yui-gen1-button").click()
time.sleep(0.5)



def checkFinished(browser,project_name):
    context =  browser.find_element_by_class_name("console-output").text
    lastStr = str(context)[-100:]
    print(">>>>>>>>>"+project_name+'正在构建......')
    if int(lastStr.find('Finished: SUCCESS')) < 0 :
        time.sleep(1)
        browser.refresh()
        checkFinished(browser,project_name)
    else:
        print(">>>>>>>>>"+project_name+'Finished: SUCCESS......')
        return

## pushtest
def pushtest(browser,project_name):
    search = browser.find_element_by_id("search-box")
    pushtest_name = "pushtest-"+project_name
    search.send_keys(pushtest_name + Keys.RETURN)
    time.sleep(0.5)
    browser.find_element_by_link_text("Build with Parameters").click()
    set_inputs = browser.find_elements_by_class_name("setting-input   ")
    for input_index in range(len(set_inputs)):
        input = set_inputs[input_index]
        input.clear()
        if input_index == 0:
            input.send_keys('wangzaogen')
        else:
            input.send_keys(project_branch.get(project_name))

    browser.find_element_by_xpath("//*[@id='ecp_dependence_2']/td/input").click()
    file = browser.find_element_by_xpath("//*[@id='main-panel']/form/table/tbody[9]/tr[1]/td[3]/div/input[2]")
    file.send_keys("D:\微信截图_20180720130557.png")
    browser.find_element_by_id("yui-gen1-button").click()
    print(">>>>>>>>>"+project_name+"正在pushtest")
    time.sleep(1)

## 开发环境构建
for project_name in build_projects:
    search = browser.find_element_by_id("search-box")
    search.clear()
    search.send_keys(project_name + Keys.RETURN)
    browser.find_element_by_link_text("立即构建").click()
    time.sleep(3)
    browser.refresh()
    build_history = browser.find_elements_by_class_name("build-link")
    href = build_history[0].get_attribute("href")
    array_url = str(href).split("/")
    his_num = array_url[len(array_url)-2]
    browser.get(constant.dev_jenkins_job_url + project_name + '/' + his_num + '/console')
    flag = checkFinished(browser,project_name)
    pushtest(browser,project_name)

