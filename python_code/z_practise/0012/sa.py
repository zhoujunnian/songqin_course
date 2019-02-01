# coding=utf8

import xlrd,xlwt

book = xlrd.open_workbook(u"中国电话区号.xls")

print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)

for rx in range(20):
    print(sh.cell_value(rx,0))


MAX_ROW_NUMBER = sh.nrows


'''
将每个省的 电话区号存储到 字典格式为 
{
    '河北省':[ ('邯郸市',‘0310’)，('石家庄',‘0311’)],
    '江西省':[ ('邯郸市',‘0310’)，('石家庄',‘0311’)],
    ....
}    
'''

retDict = {}
provinceList = []


# 先处理第一行直辖市的
# 2列一组 分析， 循环执行，直到没有数据

cur_column = 0 # 从第0列开始，每次循环 加2
while cur_column <= 10: # 最多到10列

    # 将一组（2列）信息读取到retDict中
    name = sh.cell_value(0,cur_column)
    phone_code = sh.cell_value(0,cur_column+1)
    provinceList.append(name)
    retDict[name] = [(name,phone_code)]

    cur_column +=2





def analyze_one_group(column):


    def analyze_one_province(start_row):
        '返回值 next_start_row 为负数表示，下面没有可以取的信息了'

        proviceName = None # 表示省名
        cityList = []      # 表示省级下属城市的区号信息

        cur_row = start_row

        while cur_row < MAX_ROW_NUMBER:
            # 读取当前 一行
            name = sh.cell_value(cur_row,column).strip()

            #读取到省市的名字
            if  name:
                # 如果 现在还没有省级 名称， 则必是省级名称
                if not proviceName:
                    proviceName = name
                # 否则 如果现在 已经有省级名称
                else:
                    city_area_code = sh.cell_value(cur_row,column+1)

                    # 如果读取电话区号，必是下属城市 存入 cityList
                    if city_area_code:
                        print name,city_area_code
                        cityList.append((name,city_area_code))
                    # 如果读取不到电话区号， 必是新省信息的开始，结束本次循环读取操作
                    else:
                        break

            # 读取到空格子
            else:
                # 如果 现在还没有省级 名称，继续往下读
                if not proviceName:
                    cur_row += 1
                    continue
                # 否则 一个省级城市的信息读取完毕，结束循环读取操作
                else:
                    break

            cur_row += 1

        # 如果获取到省级城市名，此次读取省级城市信息作有效，返回 cur_row 表示下次再次调用 的起始行数
        if proviceName:
            retDict[proviceName] = cityList
            provinceList.append(proviceName)
            return cur_row
        # 否则，没有读取到有效信息，返回表示
        else:
            return -1


    # 1 表示 从第2行开始， 第一行是直辖市，已经处理过了
    next_start_row = 1
    while next_start_row>=0:
        next_start_row = analyze_one_province(next_start_row)



# 2列一组 分析， 循环执行，直到没有数据

cur_column = 0 # 从第0列开始，每次循环 加2
while cur_column <= 10: # 最多到10列

    # 将一组（2列）信息读取到retDict中
    analyze_one_group(cur_column)

    cur_column +=2


for one in provinceList:
    print one


wb = xlwt.Workbook()

for provinceName in provinceList:

    province_citys = retDict[provinceName]

    ws = wb.add_sheet(provinceName)

    row = 0

    for cityname,code in province_citys:
        ws.write(row,0,cityname)
        ws.write(row,1,code)
        row += 1

wb.save('ret.xls')