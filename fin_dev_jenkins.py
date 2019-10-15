from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from constant import constant
from fin_test_deploy import get_commit_id

import time

for key, value in constant.project_of_key.items():
    print("key:{},项目名：{}\n".format(key,value))

project_key = input("请输入需要构建的项目对应的key：\n")

projects = ['gl-finance-ws','fin-erp-remote','fin-rebate-admin','gl-fin-h5','gl-finance-h5']
pro_name = constant.project_of_key.get(project_key)
build_projects = [pro_name]
if pro_name not in projects:
    print(pro_name+',项目不存在财务项目列表中')
    raise Exception("项目不存在财务项目列表中")

deploy_flag = input("是否需要deploy (y/n)：\n")

project_branch_name = input("请输入需要构建的项目分支：\n")
project_branch = {}
project_branch[pro_name] = project_branch_name

browser = webdriver.Chrome("D:\\fin_dev_jenkins\\chromedriver.exe")

browser.get(constant.dev_jenkins_login_url)
browser.minimize_window()
# build_projects = constant.build_projects
# project_branch = constant.project_branch


f = open("D:\\fin_dev_jenkins\\pwd.txt","r")
lines = f.readlines()
if(lines.__len__ == 0):
    print("用户名密码为空....")
    browser.close()
user_name = lines[0].replace("\n","")
user_pwd = lines[1]

name = browser.find_element_by_id("j_username")
pwd = browser.find_element_by_name("j_password")
name.clear()
pwd.clear()
name.send_keys(user_name)
pwd.send_keys(user_pwd)
browser.find_element_by_id("yui-gen1-button").click()

## 检查构建完成
def checkFinished(browser,project_name):
    context =  browser.find_element_by_class_name("console-output").text
    lastStr = str(context)[-100:]
    print(">>>>>>>>>"+project_name+'正在构建......')
    if int(lastStr.find('Finished: SUCCESS')) < 0 :
        time.sleep(3)
        browser.refresh()
        checkFinished(browser,project_name)
    else:
        print(">>>>>>>>>"+project_name+'Finished: SUCCESS......')
        return
## 检查是否在排队
def checkWait(browser,project_name):
    try:
        wait = browser.find_element_by_class_name("indent-multiline")
    except NoSuchElementException as e:
        return
    else:
        print(">>>>>>>>>"+project_name+'>正在排队......')
        time.sleep(5)
        browser.refresh()
        checkWait(browser,project_name)

# 获取控制台编号
def get_console_num_url(browser):
    build_history = browser.find_elements_by_class_name("build-link")
    href = build_history[0].get_attribute("href")
    array_url = str(href).split("/")
    his_num = array_url[len(array_url)-2]
    return his_num

## 测试环境构建
def test_jenkins_build(browser):
    browser.get(constant.test_dev_jenkins_login_url)
    print("test build start ......")
    name = browser.find_element_by_id("j_username")
    pwd = browser.find_element_by_name("j_password")
    name.clear()
    pwd.clear()
    name.send_keys(user_name)
    pwd.send_keys(user_pwd)
    browser.find_element_by_id("yui-gen1-button").click()
    time.sleep(1)
    ## 测试环境构建
    for project_name in build_projects:
        print(project_name+"测试环境开始构建......")
        search = browser.find_element_by_id("search-box")
        search.clear()
        search.send_keys(project_name + Keys.RETURN)
        print(project_name+">>>> test build end ......")
        time.sleep(1)
        browser.find_element_by_link_text("立即构建").click()
        time.sleep(2)
        try:
            his_num = get_console_num_url(browser)
            his_num = str(int(his_num)+1)
            browser.get(constant.test_jenkins_job_url + project_name + '/' + his_num + '/console')
            flag = checkFinished(browser,project_name)
        except Exception as e:
            print(e)
        print(project_name+"测试环境构建完成......")

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
            input.send_keys(user_name)
        else:
            input.send_keys(project_branch.get(project_name))

    browser.find_element_by_xpath("//*[@id='ecp_dependence_2']/td/input").click()
    file = browser.find_element_by_xpath("//*[@id='main-panel']/form/table/tbody[9]/tr[1]/td[3]/div/input[2]")
    file.send_keys("D:/fin_dev_jenkins/提测截图.png")
    browser.find_element_by_id("yui-gen1-button").click()
    print(">>>>>>>>>"+project_name+"正在pushtest")
    checkWait(browser,pushtest_name)
    his_num = get_console_num_url(browser)
    browser.get(constant.dev_jenkins_job_url + pushtest_name + '/' + his_num + '/console')
    flag = checkFinished(browser,pushtest_name)
    test_jenkins_build(browser)
    time.sleep(1)

def deploy(project_name):
    print("准备deploy")
    browser.get(constant.test_deploy_login_url)
    name = browser.find_element_by_id("loginform-username")
    pwd = browser.find_element_by_id("loginform-password")
    name.clear()
    pwd.clear()
    name.send_keys(user_name)
    pwd.send_keys(user_pwd)
    browser.find_element_by_name("login-button").click()
    browser.get(constant.test_deploy_task_url+constant.project_of_id.get(project_name))
    time.sleep(1)
    commit_id = get_commit_id(constant.project_of_id.get(project_name),'master')

    browser.find_element_by_id("task-commit_id").send_keys(commit_id)

    browser.find_element_by_class_name("btn-primary").click()
    time.sleep(0.5)
    browser.find_element_by_link_text('上线').click()
    time.sleep(0.5)
    browser.find_element_by_class_name("btn-deploy").click()
    print(project_name+"正在发布上线")
    time.sleep(1)

## 开发环境构建
for project_name in build_projects:
    try:
        search = browser.find_element_by_id("search-box")
        search.clear()
        search.send_keys(project_name + Keys.RETURN)
        browser.find_element_by_link_text("立即构建").click()
        time.sleep(0.5)
        browser.refresh()
        checkWait(browser,project_name)
        his_num = get_console_num_url(browser)
        browser.get(constant.dev_jenkins_job_url + project_name + '/' + his_num + '/console')
        flag = checkFinished(browser,project_name)
        pushtest(browser,project_name)
        if deploy_flag == 'y' or deploy_flag == 'Y':
            deploy(project_name)

    except Exception as e:
        print(project_name+"构建失败请检查配置.......")
        print(e)
        browser.close()

time.sleep(1)
browser.close()


