from selenium import webdriver
from constant import *
import requests

import time

url = 'http://deploy.yiyaowang.com/walle/get-commit-history?projectId={}&branch={}'


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}  # get方法其它加个ser-Agent就可以了


cookies={}

cookies['PHPSESSID'] = 'q9023o4mc1klec99cqnao8hnp0'
cookies['_identity'] = 'af654f4045af8c4fba64f73c97eb5bb651fb6d190126225ab210e96b5aa404f3a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A48%3A%22%5B283%2C%22FI6CtF9thjzr_vos4njDqP3tyynw-td5%22%2C2592000%5D%22%3B%7D'
cookies['_csrf'] = '6d76e43f634cb7015a162fecc4d18d9e0c3449bf1d34a6f6918c0ae9d2dcbe03a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22TwyByxohiRjEcqnIp3tfMYRwX9P_Vvsz%22%3B%7D'


def get_commit_id(product_id, branch):
    print("获取commit_id")
    s = requests.session()
    r = s.get(url.format(product_id,branch), headers=headers, cookies=cookies, verify=False)
    result = r.json()
    data = result["data"][0]   # 获取data里面内容
    last_commit = data['id']
    return last_commit

# browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
#
# browser.get(constant.test_deploy_login_url)
#
# name = browser.find_element_by_id("loginform-username")
# pwd = browser.find_element_by_id("loginform-password")
# print("登录deploy")
# name.clear()
# pwd.clear()
# name.send_keys(constant.user_name)
# pwd.send_keys(constant.user_pwd)
# browser.find_element_by_name("login-button").click()
#
#
# ## 测试环境构建
# for project_name in constant.build_projects:
#     browser.get(constant.test_deploy_task_url+constant.project_of_id.get(project_name))
#
#     commit_id =  get_commit_id(constant.project_of_id.get(project_name),'master')
#
#     browser.find_element_by_id("task-commit_id").send_keys(commit_id)
#
#     browser.find_element_by_class_name("btn-primary").click()
#     time.sleep(0.5)
#     browser.find_element_by_link_text('上线').click()
#     time.sleep(0.5)
#     browser.find_element_by_class_name("btn-deploy").click()
#     print(project_name+"正在发布上线")
#     time.sleep(1)











