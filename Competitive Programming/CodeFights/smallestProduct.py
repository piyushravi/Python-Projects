#https://app.codesignal.com/challenge/8FdeLisamv6cFZPAc

def ires(arr):
    minx = min(arr)
    l1 = l2 = 0
    l3 = l4 = l5 = max(arr)+1
    for x in arr:
        if x>l1:
            l2 = l1
            l1 = x
        elif x>l2:
            l2 = x
                
        if x<l3:
            l5 = l4
            l4 = l3
            l3 = x
        elif x<l4:
            l5 = l4
            l4 = x
        elif x<l5:
            l5 = x
    
    
    return min(minx*l1*l2, l5*l3*l4)
    

def smallestProduct(arr):
    
    is0 = False
    isNeg = False
    isNegPro = False
    negCount3 = None
    posCount2 = None
    minx = 0
    
    for x in arr:
        if x<minx:
            minx = x
        if x==0:
            is0 = True
        
        elif x>0:
            if posCount2==None:
                posCount2 = False
            elif not posCount2:
                posCount2 = True
            
        else:
            if isNeg:
                if negCount3==None:
                    negCount3 = False
                elif not negCount3:
                    negCount3 = True
                    return ires(arr)
            else:
                isNeg = True
                
    
    
    
    
    if isNeg and posCount2:
        return ires(arr)
    elif is0:
        return 0
    else:
        l1 = l2 = l3 = max(arr)
        
        for x in arr:
            if x<l1:
                l3 = l2
                l2 = l1
                l1 = x
            elif x<l2:
                l3 = l2
                l2 = x
            elif x<l3:
                l3 = x
        return l1*l2*l3
        
                    
    
    
    

