with open('99table.txt', 'w', encoding='utf-8') as f:
    for x in range(1, 10):
        y = 1
        while y <= x:
            cell = str(y) + '*' + str(x) + '=' + str(x * y)
            if x * y < 10:
                cell += ' '     # 对齐
            f.write(cell + ' ')
            y += 1
        f.write('\n')