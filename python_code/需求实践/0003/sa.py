def sort2(alist):
    newlist = []
    while len(alist)> 0:
        # get current min one
        theMin = alist[0]
        idx = 0       # record cur ele's idx
        minIdx = 0    # record min ele idx
        for one in alist:
            if one < theMin:
                theMin = one
                minIdx = idx
            idx += 1
        newlist.append(theMin)
        del alist[minIdx]
    return newlist
    
    
a = [3,5,7,2,56,34,54,23,21,56,33,2]
print(sort2(a))



