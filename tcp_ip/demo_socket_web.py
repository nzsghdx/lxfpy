# socket服务端

# socket依赖有四项:服务器地址,服务器端口,客户端地址,客户端端口,用于来唯一确定一个socket


# 导入所需要的包,socket用于创建tcp连接,threading用于创建线程,time设置睡眠时间
import socket
import threading
import time

# 给导入的包重命名
time=time

# 创建连接,ipv4连接,stream流
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定在本机地址的9999端口
# 不知道为什么貌似设置的端口号没有用,或者有其他我不明白的原因
s.bind(('127.0.0.1',9999))

# listen方法表示开始监听,参数5表示指定等待连接的最大数量
s.listen(5)

# 首先打印一句话
print('Waiting for connection...')


# 操作方法
def tcplink(sock,addr):
    # 服务器打印连接地址
    print('Accept new connection from %s:%s...'%addr)
    # 发送到客户端指定内容
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        # 如果不是数据或者数据内容是utf-8形式的字符串exit,那么就break
        if not data or data.decode('utf-8')=='exit':
            break
        # 向客户端发送指定形式的字符串
        sock.send(('Hello,%s!'%data).encode('utf-8'))
    # 关闭socket连接
    sock.close()
    # 关闭之后同样打印
    print('Connection from %s:%s closed.'%addr)

# 执行
while True:
    # accept函数表示接收一个新连接
    # fd, addr = self._accept()有点小错误,ctrl c关闭的时候出现的,暂时不知道原因不知道怎么解决
    sock,addr=s.accept()
    # 设置线程,target指定方法,args设置参数
    t=threading.Thread(target=tcplink,args=(sock,addr))
    # 新线程开始
    t.start()
