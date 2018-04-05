import socket

# SOCK_DGRAM表示udp协议
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# 同样是设置的端口号不管用
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999...')

while True:
    # 使用recvfrom函数获取data和addr
    # 这里的data和客户端中的字符串一致,还是客户端的和服务器的一致?
    data,addr=s.recvfrom(1024)
    # 然后服务器打印
    print('Received from %s:%s.'%addr)
    # 把指定格式的数据发送给client
    s.sendto(b'Hello,%s!'%data,addr)
