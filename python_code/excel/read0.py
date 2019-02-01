import xlrd

book = xlrd.open_workbook("fee.xlsx")

print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print(u"{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print(u"Cell A0 is {0}".format(sh.cell_value(rowx=0, colx=0)))
for rx in range(sh.nrows):
    print(sh.row(rx))



