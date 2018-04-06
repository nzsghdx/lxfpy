# 这里只有一个函数
# environ是一个包含所有http请求信息的dict对象
# start_response是一个发送http响应的函数
def application(environ,start_response):
    # 设置响应内容
    start_response('200 OK',[('Content-Type','text/html')])
    # [1:]是切片,表示从第一个到最后一个的吧?
    # 默认是web
    body='<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:]or'web')
    return [body.encode('utf-8')]
#    return [b'<h1>Hello,web!</h1>']
