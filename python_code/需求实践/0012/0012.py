#coding=gbk
import xlrd,xlwt
book=xlrd.open_workbook(u'中国电话区号.xls')
sh=book.sheet_by_index(0)
zhixiashiNamelist=[]
zhixiashiCodeList=[]
colidx1=0      #城市名字所在的列
colidx2=1       #区号所在的列
#将直辖市名字和直辖市区号分别存入列表zhixiashiNamelist和zhixiashiCodeList
while colidx1 < sh.ncols and colidx2 < sh.ncols:
     zhixiashiName= sh.cell_value(0,colidx1)
     zhixiashiNamelist.append(zhixiashiName)
     zhixiashiCode=sh.cell_value(0,colidx2)
     zhixiashiCodeList.append(zhixiashiCode)
     colidx1+=2
     colidx2+=2
     print zhixiashiName
     print zhixiashiCode
#将zhixiashiNamelist和zhixiashiCodeList中的值写入各自对应的sheet表中
workbook=xlwt.Workbook()
i=0
#遍历直辖市列表，创建直辖市命名的sheet
for one in zhixiashiNamelist:
       print type(one)
       sheet = workbook.add_sheet(one)
       sheet.write(0,0,zhixiashiCodeList[i])
       i+=1
#遍历省并建立以省命名的sheet
workbook1=xlwt.Workbook()
provicelist=[]
rows=[1,16,28,53,64]
j=0
while j < len(rows):
    colidx1=0
    while colidx1 < sh.ncols:
        proviceName=sh.cell_value(rows[j],colidx1)
        # print proviceName
        provicelist.append(proviceName)
        colidx1 += 2
    j+=1
#创建以省命名的sheet
for one1 in provicelist:
    # print one1
    sheet1=workbook1.add_sheet(one1)
workbook1.save('result2.xls')