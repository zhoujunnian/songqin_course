# coding=utf8
def bubble(alist):
    # j代表元素的下标，从最后一个元素 到 第二个元素
    for j in range(len(alist)-1,0,-1):
        # 第一轮的比较  是所有元素的比较，第二轮是 n-1 个元素
        for i in range(0, j):
            if alist[i] > alist[i+1]:
                alist[i + 1],alist[i],  =  alist[i],alist[i+1]
    return alist




a = [3,5,7,2,56,34,54,23,21,56,33,2]
print(bubble(a))











































# def sort2(alist):
#     newlist = []
#     while len(alist)> 0:
#         # get current min one
#         theMin = 2147483647
#         idx = 0
#         minIdx = 0
#         for one in alist:
#             if one < theMin:
#                 theMin = one
#                 minIdx = idx
#             idx += 1
#         newlist.append(theMin)
#         del alist[minIdx]
#     return newlist