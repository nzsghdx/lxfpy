from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

# 同一个路径下分为GET/POST请求
@app.route('/sigin',methods=['GET'])
def sigin_form():
    # 设定使用form.html
    return render_template('form.html')

@app.route('/sigin',methods=['POST'])
def sigin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)

if __name__=='__main__':
    app.run()
