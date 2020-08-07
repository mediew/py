def dth(d):
        h = ''
        n = d
        while n > 0:
                toHex = str(n%16)
                if int(toHex) >= 10:
                        toHex = chr(int(toHex) + 87)
                h = toHex + h
                n = n // 16
        return h
d = eval(input('enter a number:'))
print('The hex number is ' + dth(d))
