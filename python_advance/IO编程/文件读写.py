"""
1.打印九九乘法表如下
2.编码：若出现UnicodeDecodeError错误，则添加参数errors='ignore'
3.写文件注意：如果以'w'模式写文件则默认为覆盖原文件，若想从文件末尾追加，则以'a'模式写
"""
with open('99table.txt', 'w', encoding='utf-8') as f:
    for x in range(1, 10):
        y = 1
        while y <= x:
            cell = str(y) + '*' + str(x) + '=' + str(x * y)
            if x * y < 10:
                cell += ' '  # 对齐
            f.write(cell + ' ')
            y += 1
        f.write('\n')