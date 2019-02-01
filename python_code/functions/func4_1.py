x = 2
y = 3

def funcx():
    global x,y
    x = 9
    y = 3
    print("this x is in the funcx:-->", y)


funcx()
print("--------------------------")
print("this x is out of funcx:-->", y)

