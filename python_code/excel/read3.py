# coding=utf8
import xlrd

book = xlrd.open_workbook("fee.xlsx")

COL_DATE  = 0
COL_FEE   = 1
COL_INFO  = 2
XL_CELL_NUMBER	= 2

#查看是否有现成获取所有sheet的方法
for sheet in book.sheets():
    print sheet.name

    i = 0
    for  rowx in range(sheet.nrows):
        if i == 0:
            i += 1
            continue

        i += 1
        fee = sheet.cell_value(rowx,COL_FEE)
        if fee >= 200:
            date = sheet.cell_value(rowx,COL_DATE)
            datestr = xlrd.xldate_as_tuple(date, 0)
            info = sheet.cell_value(rowx,COL_INFO)

            print datestr,fee,info








