# collections集合模块

from collections import namedtuple,deque,defaultdict,OrderedDict
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
# 可以用属性而不是索引来引用tuple的某个元素,更方便
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))
# Circle=namedtuple('Circle',['x','y','z'])

q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)


dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

d=dict([('a',1),('b',2),('c',3)])

print(d)

od=OrderedDict([('a',1),('b',2),('c',3)])

print(od)

# 失去兴致,暂别!
