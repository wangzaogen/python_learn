import requests
import re
import time
import ctypes

## 图片文件名 local 设置为日期
local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'

## 获取必应背景图片地址
def get_bing(url):
    con = requests.get(url)
    content = con.text
    ## 通过正则表达式获取到所有已/th开头并已jpg开头的图片地址
    pattern = re.compile('/th\S*jpg')
    a = pattern.findall(content)
    ## 拼接地址
    pic_url = url + a[0]
    return pic_url

## 保存图片
def save_bing_bg_pic(pic_url):
    ## 请求图片地址
    read = requests.get(pic_url)
    ## 向D:\pic目录下写入图片文件
    f = open('D:\\pic\\%s.jpg' % local, 'wb')
    f.write(read.content)
    f.close()
    print('D:\\pic\\'+local+'.jpg')

## 设置windows桌面背景
def set_windows_bg():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:\\pic\\'+local+'.jpg', 0)

## 执行
def main():
    pic_url = get_bing(url)
    save_bing_bg_pic(pic_url)
    set_windows_bg()


main()





