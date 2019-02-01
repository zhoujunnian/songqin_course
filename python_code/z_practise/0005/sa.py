def putInfoToDict(fileName):
    retDict = {}
    with open(fileName) as f:
        lines = f.read().splitlines()
        
        for line in lines:
            # remove '(' and ')'
            line = line.replace('(','').replace(')','').replace(';','').strip()
            
            parts = line.split(',')
            ciTime     = parts[0].strip().replace("'",'')
            lessonid   = int(parts[1].strip())
            
            
            userid     = int(parts[2].strip())
            
            toAdd = {'lessonid':lessonid,'checkintime':ciTime}
            # if not in, need to create list first
            if userid not in retDict:
                retDict[userid] = []            
            retDict[userid].append(toAdd)
    
            # or just 
            #retDict.setdefault(userid,[]).append(toAdd)
    
    return retDict
    

    
ret = putInfoToDict('0005_1.txt')

import pprint
pprint.pprint(ret)