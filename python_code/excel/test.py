# coding=utf8

# 对每个sheet:
#     对每行记录：
#         获取消费金额，如果超过200，显示整条记录


import xlrd
import xlwt
book = xlrd.open_workbook("fee.xlsx")

COL_DATE = 0
COL_FEE  = 1
COL_INFO = 2

tobewrite = []
for idx  in  range(book.nsheets):
    sh = book.sheet_by_index(idx)
    print sh.name

    for rowx in range(1,sh.nrows):
        fee = sh.cell_value(rowx,COL_FEE)
        if fee >= 200:
            date = sh.cell_value(rowx, COL_DATE)
            tmp = xlrd.xldate_as_tuple(date,0)
            dateStr = "%s-%s-%s" % (tmp[0],tmp[1], tmp[2])
            info = sh.cell_value(rowx, COL_INFO)
            print dateStr,fee,info
            tobewrite.append( "%s %s %s" % (dateStr,fee,info))



workbook = xlwt.Workbook()
sheet = workbook.add_sheet("1")

idx = 0
for one in tobewrite:
    sheet.write(idx, 1, one)
    idx +=1

workbook.save("result.xls")