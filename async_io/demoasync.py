# 异步io模型需要一个消息循环,主线程不断重复'读取消息-处理消息'的过程
loop=get_event_loop()
while True:
    event=loop.get_event()
    process_event(event)
