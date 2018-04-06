def consumer():
    r=''
    while True:
        # 接收到r之后,n不为空,继续执行接下来的代码
        # 切换到consumer执行后,通过yield拿到消息(返回给来的内容),继续执行,然后又通过yield把结果返回
        n=yield r 
        if not n:
            return
        print('[CONSUMER] Consuming %s...'%n)
        # 执行到这里之后继续执行yield,所以把r='200 OK'给返回到了produce
        r='200 OK'

def produce(c):
    # 启动生成器(generator),使用send方法
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...'%n)
        # 一旦生产了东西,使用生成器切换到consumer执行
        # r接收到了返回来的信息
        r=c.send(n)
        print('[PRODUCER] Consumer return:%s'%r)
    c.close()

c=consumer()
produce(c)
