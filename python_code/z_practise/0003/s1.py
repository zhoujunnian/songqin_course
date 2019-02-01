# coding=utf8

a = [3,5,7,2,56,34,54,23,21,56,33,2]
def sort(inList):

    newList = []


    # 设计一个循环，每个循环做如下事情（直到 inlist 没有元素）：
    #     找出当前inlist中所有元素中最小curMin的，append在newList里面
    #
    #     inList 去掉 curMin

    while len(inList) > 0:
        theMin = inList[0] # 记录当前循环最小元素
        minIdx = 0   # 记录当前最小元素的下标
        idx = 0      # 指向当前元素下标
        for one in inList:
            if theMin > one:
                theMin = one
                minIdx = idx

            idx += 1

        inList.pop(minIdx)
        newList.append(theMin)

    return newList


print(sort([1, 3, 5, 7, 34, 23, 55, 56, 2, 3, 4]))
