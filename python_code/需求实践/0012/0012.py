#coding=gbk
import xlrd,xlwt
book=xlrd.open_workbook(u'�й��绰����.xls')
sh=book.sheet_by_index(0)
zhixiashiNamelist=[]
zhixiashiCodeList=[]
colidx1=0      #�����������ڵ���
colidx2=1       #�������ڵ���
#��ֱϽ�����ֺ�ֱϽ�����ŷֱ�����б�zhixiashiNamelist��zhixiashiCodeList
while colidx1 < sh.ncols and colidx2 < sh.ncols:
     zhixiashiName= sh.cell_value(0,colidx1)
     zhixiashiNamelist.append(zhixiashiName)
     zhixiashiCode=sh.cell_value(0,colidx2)
     zhixiashiCodeList.append(zhixiashiCode)
     colidx1+=2
     colidx2+=2
     print zhixiashiName
     print zhixiashiCode
#��zhixiashiNamelist��zhixiashiCodeList�е�ֵд����Զ�Ӧ��sheet����
workbook=xlwt.Workbook()
i=0
#����ֱϽ���б�����ֱϽ��������sheet
for one in zhixiashiNamelist:
       print type(one)
       sheet = workbook.add_sheet(one)
       sheet.write(0,0,zhixiashiCodeList[i])
       i+=1
#����ʡ��������ʡ������sheet
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
#������ʡ������sheet
for one1 in provicelist:
    # print one1
    sheet1=workbook1.add_sheet(one1)
workbook1.save('result2.xls')