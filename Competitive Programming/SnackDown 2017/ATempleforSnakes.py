#A Temple for Snakes

t=int(input())

for x in xrange(t):
    n=int(input())
    
    L=map(int, raw_input().split())
    
    cumL=[]
    tempC=0
    
    for y in xrange(n):
        cumL.append(0)
        cumL[y]=tempC+L[y]
        tempC=cumL[y]
        
    ind=0
    sinc=True
    lenC=0
    for y in xrange(n):
        if L[y]!=y-ind+1:
            sinc=False
            
