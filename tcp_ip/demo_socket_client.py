# 导入socket
import socket

# af_inet6则表示ipv6,sock_stream表示流
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接
s.connect(('www.sina.com.cn',80))

# 连接之后可以发送:发送请求
s.send(b'GET / HTTP/1.1\r\nHOST:www.sina.com.cn\r\nConnection:close\r\n\r\n')

# 用于临时接收存储数据
buffer=[]

while True:
    # 设置每次最大接收的数据量
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

# 把数据join到data中
data=b''.join(buffer)


# 分离接收到的head和html
header,html=data.split(b'\r\n\r\n',1)
# 打印头文件
print('............................')
print(header.decode('utf-8'))
print('............................')

# 保存网页内容到文件
with open('sina.html','wb') as f:
    f.write(html)

# 最后要关闭
s.close()
