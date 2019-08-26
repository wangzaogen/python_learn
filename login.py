from bottle import route, run, request, template, debug, redirect, default_app
from beaker.middleware import SessionMiddleware

#设置session参数
session_opts = {
    'session.type':'file',                   # 以文件的方式保存session
    'session.cookei_expires':60,       # session过期时间为3600秒
    'session.data_dir':'/tmp/sessions',  # session存放路径
    'sessioni.auto':True
}

@route("/login")
def index():
    # return 'hello world'
    return template('login.tpl',hallo='wangzaogen')


@route("/login",method='post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'wangzaogen' and password == '111111':
        s = request.environ.get('beaker.session')
        s['user'] = username
        s.save()
        return redirect("/s")
    else:
        return '<p>账户名或密码错误</p>'
    # return '<p>帐号:%s</p><p>密码:%s</p>' %(username,password)
@route('/s')
def index():
    # for k,v in request.environ.items():
    #     print ("K:%s     V:%s" %(k,v))
    s = request.environ.get('beaker.session') #获取session
    for k,v in s.items():
        print ("K:%s     V:%s" %(k,v))
    username = s.get('user',None)   #从session中获取Key为user的值，是上面登陆的时候保存进来的
    if not username:
        return redirect('/login')
    return "欢迎你：%s" % username

@route("/info")
def info():
    name = request.query.name
    age = request.query.age
    return '<p>name=%s,age=%s</p>' %(name,age)

debug(True)
app = default_app()
app = SessionMiddleware(app, session_opts)
run(app=app,host='127.0.0.1',port=8080,reloader=True)