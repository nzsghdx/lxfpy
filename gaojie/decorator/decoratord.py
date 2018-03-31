def log(func):
    def wrapper(*args,**kw):
        # 函数使用单引号的吗,还以为是那个``
        print('call %s()'%func.__name__)
        return func(*args,**kw)
    return wrapper

# 相当于now=log(now)
@log
def now():
    print('Hello Decorator!')


now()
