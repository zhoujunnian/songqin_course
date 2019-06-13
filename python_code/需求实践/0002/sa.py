# https://github.com/jcyrss/songqin-testdev/blob/master/python/task/task02.md

# Jack Green ,   21  ;  Mike Mos, 9;
inputStr = input('Please input student age info:')
studentInfo = inputStr.split(';')
for one in studentInfo:
    # check if it is valid input 
    if ',' not in one: 
        continue
        
    name,age = one.split(',')
    name = name.strip()
    age  = age.strip()
    
    #  check is age digit
    if not age.isdigit():
        continue
    
    age = int(age)

    print('%-20s :  %02d' % (name, age))
    # print('{:20} :  {:02}'.format(name, age))
    # print(f'{name:20} :  {age:02}')


