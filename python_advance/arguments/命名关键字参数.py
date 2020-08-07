# 1.关键字参数可以传入不受限制的关键字，命名关键字参数只能传入特定key的参数
def person(name, age, *, gender, city):
    print(name, age, gender, city)

# 2.注意，函数定义的时候需要加特殊的分隔符   ，*，和关键字参数的形式不同
person('Meachael', 30, gender='F', city='Beijing')
# Meachael 30 F Beijing

'''
# 3.必须严格按照要求传入
person('Meachael', 30, gender='F')
# TypeError: person() missing 1 required keyword-only argument: 'city'
person('Meachael', 30, gender='F', c='Beijing')
# TypeError: person() got an unexpected keyword argument 'c'

# 4.命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person('Jack', 24, 'F', 'Beijing')
# TypeError: person() takes 2 positional arguments but 4 were given
# Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数
'''

# 5.命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, gender, city='Beijing'):
    print(name, age, gender, city)

person('Meachael', 30, gender='F')
# Meachael 30 F Beijing

# 6.如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)