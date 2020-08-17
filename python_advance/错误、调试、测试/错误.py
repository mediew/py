try:
    print('try...')
    r = 10 / int('0')
    print('result:', r)                     # 无错误时执行
except ValueError as e:
    print('ValueError:', e)                 # 错误类型为ValueError时执行
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)          # 错误类型为ZeroDivisionError时执行
else:
    print('no error!')                      # 没有错误时执行
finally:
    print('finally...')                     # 无论有无错误均会执行
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
def foo():
    r = 0
    if r==(-1):
        return (-1)
    # do something
    return r

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

# Python内置的logging模块可以非常容易地记录错误信息：
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。