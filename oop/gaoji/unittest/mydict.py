# 自定义的一个类,为了完成单元测试练习
class Dict(dict):
    def __init__(self,**kw):
        #super是表示继承自父类的**kw,应该是dict的内置的吧,乱七八糟,很迷
        super().__init__(**kw)

    # 一边学一边忘,这两个getattr和setattr是干嘛用的 
    def __getattr__(self,key):
        try:
            # 获取key的时候直接返回,报错则进入except部分
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)

    def __setattr__(self,key,value):
        # 设置的话则直接放到当前key
        self[key]=value


