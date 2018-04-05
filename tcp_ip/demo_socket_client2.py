import socket 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 客户端使用connect来连接
s.connect(('127.0.0.1',9999))

# 接收到的数据按照utf-8的格式打印
print(s.recv(1024).decode('utf-8'))

# 不知道字母b是干嘛的..
# 从给定的数据中遍历,然后发送到服务器(因为连接了服务器,所以send到了服务器)
for data in [b'Michael',b'Tracy',b'Sarah']:
    # 在服务器上也是send,不知道具体操作是怎么回事,但是结果就是打印了hello data..,互相发送然后自动结合?
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

# 执行完了之后断开连接
s.send(b'exit')
# 关闭socket
s.close()
