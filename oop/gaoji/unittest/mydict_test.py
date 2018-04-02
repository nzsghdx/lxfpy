import unittest
# 从mydict文件中导入Dict类
from mydict import Dict

# 测试类
class TestDict(unittest.TestCase):
    def test_init(self):
        # 导入过来的Dict中有两个参数,第一个是它本身,第二个表示任意个关键字参数,这里的d里面有两个关键字参数a和b
        d=Dict(a=1,b='test')
        # 判断d.a和1是否相同
        self.assertEqual(d.a,1)
        # 运行过程中什么都不会输出,用print也没用
        # 但是可以在运行脚本的时候使用参数: python3 -m unittest mydict_test
#        print(self.assertEqual(d.a,1))
        # 判断d.b和test是否相同
        self.assertEqual(d.b,'test')
        # 判断d是否是dict类型的
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        # 赋值,key=key,value=value
        d['key']='value'
        # 判断d.key和value是否相同
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=Dict()
        # 另外一种赋值方式
        d.key='value'
        # 判断key的值'key'是否在d中
        self.assertTrue('key' in d )
        # 通过'key'取value:d['key']和'value'相比判断是否相同
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrerror(self):
        d=Dict()
        # 看不懂
        with self.assertRaises(AttributeError):
            value=d.empty

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

if __name__=='__main__':
    unittest.main
