import asyncio

@asyncio.coroutine
def wget(host):
    # 首先打印正在获取的host地址
    print('wget %s...'%host)
    # 恩...打开连接?
    connect=asyncio.open_connection(host,80)
    # 中断,获取到信息之前继续执行eventloop中的其他coroutine
    reader,writer=yield from connect
    # 设置header,有点迷
    header='GET / HTTP/1.0\r\nHost:%s\r\n\r\n'%host
    # 把header写出来?
    writer.write(header.encode('utf-8'))
    # 中断,writer.drain()刷新底层写缓冲区,把需要发送的数据从缓冲区发送出去(清空队列)
    yield from writer.drain()
    while True:
        # 依次读取reader中的每一行并打印
        line=yield from reader.readline()
        if line==b'\r\n':
            break
        print('%s header>%s'%(host,line.decode().rstrip()))
        writer.close()

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
