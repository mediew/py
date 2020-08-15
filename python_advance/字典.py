# 字典的迭代
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
# 迭代dict的键
for x in d.keys():
    print(x)
# 也可以采用这种方式迭代
for x in d.iterkeys():
    print(x)
# 迭代dict的值
for x in d.values():
    print(x)
for x in d.itervalues():
    print(x)
# 迭代键值对
for k, v in d.items():
    print(k, ":", v)
for k, v in d.iteritems():
    print(k, ":", v)