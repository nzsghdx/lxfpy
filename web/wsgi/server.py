# 从wsgiref.simple_server中导入make_server
from wsgiref.simple_server import make_server
# 从hello文件中导入application
from hello import application

# 创建服务器,ip为空,端口为8000,处理函数是application
httpd=make_server('',8000,application)

print('Serving HTTP on port 8000...')

# 人家说这是开始监听http请求
# 会输出一些内容,请求的信息啊啥的
httpd.serve_forever()
