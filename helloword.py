from bottle import route, run ,request,template,debug

import requests

@route("/")
def index():
    # return 'hello world'
    return template('hallo.tpl',hallo='wangzaogen')

#带参数的静态路由
@route("/hello/:your_word", methods=['GET', 'POST'])
def hello_world(your_word):
    return template('hallo.tpl',hallo=your_word)

#动态路由
@route("/hi/<name>")
def hi(name):
    return template('hallo.tpl',hallo=name)


@route('/add', method='POST')
def add():
    cnt = requests.forms.get('txtadd')
    print(cnt)

debug(True)
run(host='127.0.0.1',port=8080,reloader=True)