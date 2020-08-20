import pickle
import json

# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等,序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)  # 序列化成bytes
with open('dp.txt', 'wb') as f:
    pickle.dump(d, f)  # pickle.dump()直接把对象序列化后写入一个file-like Object
with open('dp.txt', 'rb') as f:
    dl = pickle.load(f)
print(dl)

# json.dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
dj = json.dumps(d)  # json.dumps()提供了一个ensure_ascii参数，当含有中文时要将其设置为False
with open('dj.txt', 'w') as f:  # 此时不能以'wb'模式写入，因为dump是把dumps返回的字符串写入文件
    json.dump(dj, f)


# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


"""
运行代码，毫不留情地得到一个TypeError：
>>> s = Student('Bob', 20, 88)
>>> print(json.dumps(s))
Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
错误的原因是Student对象不是一个可序列化为JSON的对象
可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
"""


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


"""
这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
>>> print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}
我们可以偷个懒，把任意class的实例变为dict：
>>> print(json.dumps(s, default=lambda obj: obj.__dict__))
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
也有少数例外，比如定义了__slots__的class。
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例：
"""


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


"""
运行结果如下：
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
打印出的是反序列化的Student实例对象。
"""
