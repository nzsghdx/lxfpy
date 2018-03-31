# *args/**kw


# *args表示任意多个无名参数,是一个tuple
# *kwargs表示关键字参数(和无名参数对应,kw可以理解为key-word,key是word的名),是一个dict
# *args 和 *kwargs同时存在时,*args要在*kwargs前面,否则报错
def foo(*args,**kwargs):
    print('args=',args)
    print('kwargs=',kwargs)
    print('-----------------')



if __name__=='__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4,a=1,b=2,c=3)
    foo('a',1,None,a=1,b='2',c=3)
#    foo(a=1,b='2',c=3,1,None,'a')
