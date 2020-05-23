###########################################
# cyk algorithm
###########################################

import sys

### save production rule ###

ruleMap = {} # empty dictionary

print("---Context-Free Grammar Test---")
ruleCnt = int(input('규칙의 개수: '))
print('규칙을 입력하세요: ')

for i in range(ruleCnt):
    instr = input()
    str = instr.split('>')
    if len(str) == 2:
        key = str[1]
        lst = ruleMap.get(key)
        if not lst: # not in list
            lst = [str[0]]
            ruleMap[key] = lst
        else: # in list
            lst.append(str[0])
    else:
        print('input error!!!') # input error handling
        sys.exit()
            
### parse into substring ###
parseVarMap = {} # empty dictionary
w = input('멤버 확인이 필요한 문자열: ')
wlen = len(w)

for leng in range(1, wlen+1):
    for i, j in zip(range(1, wlen-leng+2), range(leng, wlen+1)):
        newkey = (i, j)
        newVars = []
        
        if leng == 1: # case 11, 22, 33, 44, 55, ...
            findkey = w[i-1]
            ruleVar = ruleMap.get(findkey)
            
            if not ruleVar:
                continue
            
            for var in ruleVar:
                newVars.append(var)
                
            parseVarMap[newkey] = newVars
            
        else: # case leng >= 2, union(V(i, k), V(k+1, j))
             for k in range(i, j):
                 key1 = (i, k)
                 key2 = (k+1, j)
                 
                 if not (parseVarMap.get(key1) and parseVarMap.get(key2)):
                        continue
                
                 for var1 in parseVarMap.get(key1):
                     for var2 in parseVarMap.get(key2):
                         findkey = var1 + var2
                         ruleVar = ruleMap.get(findkey)
                         if not ruleVar:
                             continue
                        
                         for var in ruleVar:
                             if not var in newVars: # not in list, append
                                 newVars.append(var)
                                
                         parseVarMap[newkey] = newVars
                
                
### check whether 'S' is in the last list ###
lastkey = (1, wlen)
lastvars = parseVarMap.get(lastkey)

if lastvars and ('S' in lastvars):
    print('Accept')
else:
    print('Reject')