t = int(input())

for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))

    A = L[::2]
    B = L[1::2]
    A.sort()
    B.sort()
    res = -1
    C = [-1]*n
    for x in range(n):
        if x%2:
            C[x] = B[x/2]
        else:
            C[x] = A[x/2]
    for x in range(n-1):
        if C[x]>C[x+1]:
            res = x
            break

    if res==-1:
        print 'Case #'+str(_+1)+': OK'
    else:
        print 'Case #'+str(_+1)+': '+str(res)
