'''
Problem description

Given three variables k, L, H
k - numerical base used in this problem. 2 <= k <= 16
L, H - value range of the integer to be converted. 

Closure number: how many closed areas in a number or alphabet. 0:1, H:0
return sum of the closure numbers
'''

def baseStringCounter(x, k, baseStrCnt):
    if x < k:
        baseDict[baseStr[x]] += 1
    else:
        baseDict[baseStr[x%k]] += 1
        baseStringCounter(x//k, k, baseDict)    
    
if __name__ == '__main__':
    baseStr = "0123456789ABCDEF"
    closureCnt = [1,0,0,0,1,0,1,0,2,1,1,2,0,1,0,0]
    baseStrCnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    closureDict = {x:y for x, y in zip(baseStr, closureCnt)}
    baseDict = {x:y for x, y in zip(baseStr, baseStrCnt)}
    
    L = 7
    H = 10000000
    
    for i in range(L, H+1):
        baseStringCounter(i, 16, baseDict)
        
    cntSum = 0
    for s in baseStr:
        cntSum += baseDict[s] * closureDict[s]
    print (cntSum)