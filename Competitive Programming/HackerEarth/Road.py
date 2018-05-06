#January Circuits 2018
# https://www.hackerearth.com/challenge/competitive/january-circuits-18/algorithm/road-1-63e2e618/

def result(D, V, init, k):
    
    res = 0
    
    res += D[init]
    V.append(init)
    
    if k == 0:
        return res
    
    r = 0
    for r in xrange(1, k+1):
        if init+r<51:
            if init+r not in V:
                break
        else:
            r = 0
            break
    l = 0
    for l in xrange(1, k+1):
        if init-l>=0:
            if init-l not in V:
                break
            
        else:
            l = 0
            break
        
    if l==0 and r==0:
        return res
    
    if l!=0 and r==0:
        return res+result(D, V[:], init-l, k-l)
    
    if r!=0 and l==0:
        return res+result(D, V[:], init+r, k-r)
        
    return res+max(result(D, V[:], init+r, k-r), result(D, V[:], init-l, k-l))
   
    
    
    



n, key = map(int, raw_input().split())


L = map(int, raw_input().split())

dist = {}

res = 0
        
for x in xrange(51):
    dist[x] = 0

for x in L:
    dist[x] += 1





    
print result(dist, [], L[0], key)
