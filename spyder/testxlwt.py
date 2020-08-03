import xlwt
# 打印乘法口诀表
def multisheet():
    bookwork = xlwt.Workbook(encoding = 'utf-8')
    worksheet = bookwork.add_sheet('sheet1')
    for x in range(1,10):
        for y in range(x,10):
            worksheet.write(y-1, x-1, str(x)+'x'+str(y)+'='+str(x * y))
    # worksheet.write(0,0,'hello')
    bookwork.save('testxlwt.xls')
    

'''
# 测试
savepath = 'movie250.xls'
data = 1
def saveData2xls(data, savepath):
    book = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = book.add_sheet('dbmovie250', cell_overwrite_ok = True)
    firstRow = ['排名', '中文名', '其他名', '评分', '概述', '电影详情页', '电影海报']
    for c in range(7):
        sheet.write(0, c, firstRow[c])
    for fc in range(250):
        sheet.write(fc + 1, 0, fc + 1)
    for n in range(len(data)):
        sheet.write(n + 1, 1, data[n]['cntitle'])
        sheet.write(n + 1, 2, data[n]['othertitle'])
        sheet.write(n + 1, 3, data[n]['rate'])
        sheet.write(n + 1, 4, data[n]['inq'])
        sheet.write(n + 1, 5, data[n]['infolink'])
        sheet.write(n + 1, 6, data[n]['piclink'])
    book.save(savepath)
'''


if __name__ == '__main__':
    saveData2xls(data, savepath)
