inFileName  = 'file1.txt'
outFileName = 'file2.txt'

with open(inFileName) as ifile, open(outFileName,'w') as ofile:


    beforeTax = ifile.read().splitlines()
    # 或者也可以   beforeTax = ifile.read().split('\n')
    for one in beforeTax:
        if one.count(';') != 1: # ensure valid
            continue
        
        namePart,salaryPart = one.split(';')   
        # name Part like  name: Jack  |  salaryPart like    salary:  12000]
        
        if namePart.count(':') != 1: # ensure valid
            continue
        if salaryPart.count(':') != 1: # ensure valid
            continue

        name   = namePart.split(':')[1].strip()
        salary = int(salaryPart.split(':')[1].strip())

        income = int(salary*0.9)
        tax    = int(salary*0.1)

        outPutStr = f'name: {name:>10}   ;    salary:  {salary:6} ;  tax: {tax:6} ; income:  {income:6}'

        print(outPutStr)

        ofile.write(outPutStr + '\n')
    
