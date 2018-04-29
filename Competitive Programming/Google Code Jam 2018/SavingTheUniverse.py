'''
6
1 CS
2 CS
1 SS
6 SCCSSC
2 CC
3 CSCSS
'''
t = int(input())


def damage(S, D, n):
    minD = 0
    actD = 0
    ctr = 1
    res = 0
    
    ctrL = []
    cL = []
    for x in xrange(n):
        if S[x]=='S':
            minD += 1
            actD += ctr
        else:
            ctr *= 2
            
            cL.append(x)
        ctrL.append(ctr)
        
    if minD > D:
        return 'Impossible'
    if actD<=D:        
        return res    
    
    cL = cL[::-1]
    #print actD, D
    ctr = 0
    for c in cL:
        if actD-((n-1-c-ctr)*(ctrL[c]/2))<=D:
            if (D-actD)%(ctrL[c]/2)==0:
                return res+((actD-D)/(ctrL[c]/2))
            else:
                return ((actD-D)/(ctrL[c]/2))+1+res
        else:
            actD -= ((n-1-c-ctr)*(ctrL[c]/2))
            res += n-1-c-ctr
        ctr+=1
     
    return res

        
    
    
    
    
    
        
    

for _ in xrange(t):
    D, S = raw_input().split()
    D = int(D)
    S = list(S)
    
    print "Case #"+str(_+1)+': '+str(damage(S, D, len(S)))
    
    
