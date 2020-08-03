def str2float(s):
    s = list(s)
    l = len(s)
    i = 0
    while s[i]!='.':
        i=i+1
    Digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def str2num(a):
        return Digits[a]
    def num2int(x,y):
        return 10*x+y
    from functools import reduce
    f=reduce(num2int,map(str2num,s[:i]))
    b=reduce(num2int,map(str2num,s[i+1:]))
    return f+b/10**(l-i-1)
