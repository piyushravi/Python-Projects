'''
https://www.codechef.com/SNCKQL17/problems/SNAKEEAT
'''

def binSearch(num, N):
    if num>=L[N-1]:
        if num==L[N-1]:
            return N-2
        return N-1
    
    if num<=L[0]:
        return -1
    
    lo=0
    hi=N-1
   
    while lo<hi:
        mid=lo+hi
        mid/=2
        
      
        if L[mid]<num:
            if mid+1<N:
                if L[mid+1]>=num:
                    return mid
                else:
                    lo=mid+1
                
        if L[mid]>num:
            if mid-1>-1:
                if L[mid-1]<num:
                    return mid-1
            hi=mid

        
def binSearch2(num, N, ind):
    res=N-ind-1
    
    CF=[]
    for y in xrange(ind+1):
        CF.append(0)
    CF[0]=L[0]
    
    for y in xrange(1, ind+1):
        CF[y]+=CF[y-1]+L[y]
    
    lo=0
    hi=ind
    ans=0
    prevmid=-1
    while lo<hi:

        mid=lo+hi
        mid/=2
        if mid==prevmid:
            return mid
        if (CF[ind]-CF[mid])-(num*(ind-mid))==mid-1:
            return mid
        if (CF[ind]-CF[mid])-(num*(ind-mid))-mid+1>0:
            if (CF[ind]-CF[mid-1])-(num*(ind+1-mid))-mid+2<0:
                return mid
            hi=mid
            
        else:
            lo=mid
            
        prevmid=mid    
    return ans    

def answer(num, N):
    res=0
    ind=binSearch(num, N)
 
    if ind==-1:
        return N
    else:
        res=ind-binSearch2(num, N, ind)
             
    return res            
                
         
                
            
        
    
    

t=int(input())

for x in xrange(t):
    n, q=map(int, raw_input().split())
    L=map(int, raw_input().split())
    L.sort()
    
    
        
        
    for y in xrange(q):
        print answer(int(input()), n)
        
