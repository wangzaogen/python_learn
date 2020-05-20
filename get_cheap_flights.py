import requests
import json


url = "https://wx.17u.cn/cheapflights/bffapi/cheapflightapi/cheapselect/domestic"

params = {"oc":"SHA","userTag":1}

rs = requests.post(url,params)
print(rs.status_code)
print(rs.json())