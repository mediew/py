'''
#我的答案
def is_palindrome(n):
    s=str(n)
    l=len(s)
    y=''
    for x in range(0,l):
        y=y+s[l-x-1]
    if y==s:
        return n
'''
#最佳答案
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 10000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')