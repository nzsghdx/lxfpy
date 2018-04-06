from flask import Flask
from flask import request

# 初始化flask
app=Flask(__name__)

# @是装饰器的用法
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/sigin',methods=['GET'])
def singin_from():
    return '''<form action="/sigin" method="post">
            <p><input name="username"></p>
            <p><input name="password" type="password"></p>
            <p><button type="submit">Sign in</button></p>
            </form>'''


@app.route('/sigin',methods=['POST'])
def sigin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__=='__main__':
    app.run()
