import threading
import asyncio

@asyncio.coroutine
def hello():
    # 由打印结果可知,是同一个线程
    print('Hello world!(%s)'%threading.currentThread())
    # 因为调用了两次,第一次执行到这里的时候中断,然后继续调用下一个coroutine
    # 调用的第二次执行到这里的时候,同样也中断,得到返回结果前继续调用下一个coroutine,因为eventloop里面只有两个coroutine,所以什么都不执行
    # 得到返回结果一秒之后,继续执行下一行语句,因为调用了两次hello(),所以打印了两次Hello again!.
    yield from asyncio.sleep(1)
    print('Hello again!(%s)'%threading.currentThread())

loop=asyncio.get_event_loop()
# 把同一个协程调用了两次
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
