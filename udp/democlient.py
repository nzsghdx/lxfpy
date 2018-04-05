import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for data in [b'Michael',b'Tracy',b'Sarah']:
    # 把获取到的data通过sendto函数发送到服务器
    s.sendto(data,('127.0.0.1',9999))
    # 然后使用recv函数接收数据并且同时设置编码格式
    print(s.recv(1024).decode('utf-8'))

# 最后关闭socket
s.close()
