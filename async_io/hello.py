import asyncio

# 把一个generator标记成为一个coroutine
# @asyncio.coroutine
# def hello():
  #   print('Hello Asyncio!')
    # 异步调用
    # 人家说asyncio.sleep()也是一个coroutine,所以线程不会等待asyncio.sleep(),而是直接中断,当asyncio.sleep()返回时,线程就可以从yield from中拿到值(这里是None),然后接着执行下一行语句
    # 那就是中断了一秒?返回了None之后继续执行下一行?
    # 中断之后,在得到返回内容之前,线程去执行eventloop中其他可以执行的coroutine了
   #  r=yield from asyncio.sleep(1)
   #  print('Hello Again!')


# python3.5之后提供了async和await方法,简化代码
# 不过怎么设置coroutine?自动的吗,不用手动编写吗?
async def hello():
    print('Hello Asyncio!')
    r=await  asyncio.sleep(1)
    print('Hello Again!')


# 获取eventloop
# 从asyncio模块中直接获取eventloop的引用,然后把需要执行的协程扔到eventloop中执行
# loop是循环的意思
loop=asyncio.get_event_loop()
# 执行coroutine(协程)
loop.run_until_complete(hello())
loop.close()

