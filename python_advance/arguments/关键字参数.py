# 1.关键字参数非必选
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
# name: Michael age: 30 other: {}
person('Meachal', 30, gender='F')
# name: Meachal age: 30 other: {'gender': 'F'}
person('Meachael', 30, gender='F', city='Beijing')
# name: Meachael age: 30 other: {'gender': 'F', 'city': 'Beijing'}
'''
可见，所谓关键字参数就是在传入一个值（value）的时候，必须传入键（key），故为关键字参数
传入关键字参数后，Python解释器自动转换为dict
'''
# 2.简化写法
kw = {'gender': 'F', 'city': 'Beijing'}
person('Meachael', 30, **kw)
# name: Meachael age: 30 other: {'gender': 'F', 'city': 'Beijing'}

# 3.发散
d = dict(name='Meachael', age=30)
print(d)
# {'name': 'Meachael', 'age': 30},可见函数dict的参数为关键字参数
