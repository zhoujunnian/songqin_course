x = 2

def funcx():
    global x
    x = 9
    print("this x is in the funcx:-->", x)


funcx()
print("--------------------------")
print("this x is out of funcx:-->", y)

