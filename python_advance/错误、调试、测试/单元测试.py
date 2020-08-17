# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)            # 接受判断表达式
        self.assertEqual(d['key'], 'value')    # 接受两个参数

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']                # 接受一个空的key，期待报错KeyError，with语句会抛出KeyError

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty                   # 接受一个空的attr，期待报错AttributeError，with语句会抛出AttributeError

    # setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()