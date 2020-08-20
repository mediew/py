from io import StringIO
from io import BytesIO


# StringIO只能操作str
f = StringIO()
f.write('Hello')
f.write(',')
f.write('world！')
print(f.getvalue())
print('*' * 50)
fs = StringIO('hello\nworld')
while True:
    s = fs.readline()
    if s == '':
        break
    print(s.strip())


# BytesIO可以操作二进制
fb = BytesIO()
fb.write('hello,world'.encode())
print(fb.getvalue())