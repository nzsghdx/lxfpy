# 三层
def log(text):
    # 这是一个装饰器,返回wrapper
    def decorator(func):
        # 装饰器里面有个函数,此函数返回所执行的函数名
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    # 返回装饰器给log函数
    return decorator

# 调用装饰器
@log('execute')
def now():
    print('2018-04-1')

# 执行函数
now()
