import os


# 查看环境变量
print(os.environ)    # 结果是字典
# 获取某个环境变量的值
print(os.environ.get('PATH'))

# 操作文件和目录
os.path.abspath('.')      # 查看当前目录的绝对路径
new_dir = os.path.join('newdir')    # 组装新目录的绝对路径
os.mkdir(new_dir)                   # 创建新目录
os.rmdir(new_dir)                   # 删除新目录
os.path.split('/Users/michael/testdir/file.txt')        # 拆分目录，('/Users/michael/testdir', 'file.txt')
os.path.split('file.txt')           # ('', 'file.txt')  文件永远是tuple[1]
os.path.split('/Users/michael/testdir/')                # ('/Users/michael/testdir', '')最后一个字符带/识别为文件夹
os.path.split('/Users/michael/testdir')                 # ('/Users/michael', 'testdir')最后一个字符不带/识别为文件
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
os.rename('test.txt', 'test.py')    # 重命名文件
os.remove('test.py')                # 删除文件

# 列出当前目录所有的目录
[x for x in os.listdir('.') if os.path.isdir(x)]
# 列出当前目录所有的文件
[x for x in os.listdir('.') if os.path.isfile(x)]
# 列出所有的*.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']